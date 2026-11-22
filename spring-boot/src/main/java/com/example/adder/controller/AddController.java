package com.example.adder.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/v1") // <-- remove this line if you want the URL to be just /add
public class AddController {

    // GET: /api/v1/add?a=10&b=20   (or /add if you removed @RequestMapping above)
    @GetMapping("/add")
    public ResponseEntity<AddResult> addGet(@RequestParam double a,
                                            @RequestParam double b) {
        return ResponseEntity.ok(new AddResult(a, b, a + b));
    }

    // DTOs
    public static class AddRequest {
        private double a;
        private double b;
        public double getA() { return a; }
        public void setA(double a) { this.a = a; }
        public double getB() { return b; }
        public void setB(double b) { this.b = b; }
    }

    public static class AddResult {
        private final double a;
        private final double b;
        private final double result;
        public AddResult(double a, double b, double result) {
            this.a = a; this.b = b; this.result = result;
        }
        public double getA() { return a; }
        public double getB() { return b; }
        public double getResult() { return result; }
    }
}
