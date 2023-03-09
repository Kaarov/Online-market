package com.example.university.controller;

import  com.example.university.model.Student;
import  com.example.university.repository.StudentRepository;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
public class StudentController {

    private final StudentRepository repo;

    public StudentController(StudentRepository repo) {
        this.repo = repo;
    }

    @GetMapping("/students")
    Iterable<Student> getAllStudents() {
        return repo.findAll();
    }

    @GetMapping("/students/{id}")
    Student getOneStudent(@PathVariable Long id) {
        return repo.findById(id).orElseThrow();
    }

    @PostMapping("/students")
    Student addStudent(@RequestBody Student student) {
        repo.save(student);
        return student;
    }

    @DeleteMapping("/students/{id}")
    void deleteStudent(@PathVariable Long id) {
        try {
            repo.deleteById(id);
        } catch (EmptyResultDataAccessException e) {
            System.err.println("No such id to delete");
        }
    }

    @PutMapping("/students/{id}")
    Student updateStudent(@RequestBody Student newStudent, @PathVariable Long id) {
        return repo.findById(id).map(
                student -> {
                    student.setGpa(newStudent.getGpa());
                    student.setName(newStudent.getName());
                    student.setGroup_name(newStudent.getGroup_name());
                    return repo.save(student);
                }
        ).orElseGet(() -> {
            newStudent.setId(id);
            return repo.save(newStudent);
        });
    }
}
