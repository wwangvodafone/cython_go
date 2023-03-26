package main

import (
    "fmt"
    "os/exec"
)

func main() {
    // 启动 Python 解释器
    cmd := exec.Command("python3", "copy_files.py", "--folder", "/home/wwang/cython/cython/log/")

    // 将 Python 的标准输出管道连接到 Go 的标准输出
    stdout, err := cmd.StdoutPipe()
    if err != nil {
        fmt.Println(err)
        return
    }
    defer stdout.Close()

    // 启动 Python 解释器
    if err := cmd.Start(); err != nil {
        fmt.Println(err)
        return
    }

    // 读取 Python 的输出并打印到控制台
    result := make([]byte, 100)
    n, err := stdout.Read(result)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(result)
    fmt.Printf("Result: %s", result[:n])
}
