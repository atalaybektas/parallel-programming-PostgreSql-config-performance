# PostgreSQL Performance Analysis: Optimized vs. Misconfigured Setups

This project presents a performance analysis of the PostgreSQL database by comparing **optimized** and **misconfigured** configurations. The study investigates how various PostgreSQL configuration parameters influence:

- The execution of **parallel queries** using Python threads  
- **CPU and memory utilization** during query processing

The goal is to evaluate the efficiency of configuration settings in enabling multi-threaded operations and ensuring effective system resource usage.

## 🛠 Tools & Technologies

- **Oracle VirtualBox** – for creating isolated virtual environments  
- **Ubuntu 22.04 LTS** – as the operating system on virtual machines  
- **PostgreSQL 17** – the database system under test  
- **Python** – using `concurrent.futures` for threading and `psutil` for resource monitoring  
- **Linux utilities** – `top` and `htop` for real-time system performance tracking

##  Summary

Two virtual servers with identical hardware specs (8 GB RAM, 4 CPU cores) were used:
- One with **optimized PostgreSQL configuration**
- One with **intentionally misconfigured parameters**

A set of parallel query executions was run on each setup, and performance metrics were collected and compared to highlight the impact of configuration quality.

---


