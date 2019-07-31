package main

import (
  // "log"
  "net/http"
  "google.golang.org/appengine"
)

func main() {
  fs := http.FileServer(http.Dir("flask"))
  http.Handle("/", fs)

  // log.Println("Listening...")
  // http.ListenAndServe(":3000", nil)
  appengine.Main()
}