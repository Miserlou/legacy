//
//  Package.swift
//  Legacy 
//
//
//===----------------------------------------------------------------------===//
//
//
//===----------------------------------------------------------------------===//
//
import PackageDescription

var urls = [String]()

#if os(Linux)
urls += ["https://github.com/Miserlou/legacy.git"]
#else

#endif

let package = Package(
	name: "Legacy",
	targets: [],
	dependencies: urls.map { .Package(url: $0, majorVersion: 2) },
	exclude: []
)
