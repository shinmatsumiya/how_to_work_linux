package main

import (
    "fmt"
    "log"
    "os"
    "os/exec"
    "strconv"
    "syscall"
)

const (
    ALLOC_SIZE = 1024 * 1024 * 1024
)

func main() {
    pid := os.Getpid()
    fmt.Println("*** memory map before acquiring new memory ***")
    command := exec.Command("cat", "/proc/" + strconv.Itoa(pid) + "/maps")
    command.Stdout = os.Stdout
    err := command.Run()
    if err != nil {
        log.Fatal("fail to execute cat")
    }

    // acquire 1gb memory map by call mmap
    data, err := syscall.Mmap(-1, 0, ALLOC_SIZE, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_ANON|syscall.MAP_PRIVATE)
    if err != nil{
        log.Fatal("fail to mmap()")
    }
    fmt.Println("")
    fmt.Printf("*** new memory range: address = %p, size = 0x%x ***\n", &data[0], ALLOC_SIZE)
    fmt.Println("")

    fmt.Println("*** memory map after acquiring new memory ***")
    command = exec.Command("cat", "/proc/" + strconv.Itoa(pid) + "/maps")
    command.Stdout = os.Stdout
    err = command.Run()
    if err != nil {
        log.Fatal("fail to execute cat")
    }
}

