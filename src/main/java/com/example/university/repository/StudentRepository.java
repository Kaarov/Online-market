package com.example.university.repository;

import com.example.university.model.Student;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface StudentRepository extends CrudRepository<Student, Long> {
    public List<Student> findByGpaGreaterThanOrderByGpaDesc(Double gpa);
    public List<Student> findByNameLike(String name);
}
