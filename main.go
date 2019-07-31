package main

import (
  "net/http"
  "google.golang.org/appengine"
)

func main() {
  fs := http.FileServer(http.Dir("flask"))
  http.Handle("/", fs)

  // http.ListenAndServe(":3000", nil)
  appengine.Main()
}