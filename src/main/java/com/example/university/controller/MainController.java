package com.example.university.controller;

import com.example.university.repo.StudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class MainController {

    @Autowired
    StudentRepository studentRepository;

    @GetMapping("/")
    public String main(Model model) {
        model.addAttribute("students", studentRepository.findAll());
        return "index";
    }
}
