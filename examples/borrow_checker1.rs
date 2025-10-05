use std::mem::{drop};

struct Resource {
    data: Box<i32>,
}

impl Resource {
    fn new(data: i32) -> Self {
        Self { data: Box::new(data) }
    }

    fn data(&self) -> &i32 {
        &self.data
    }
}

fn main() {
    let foo = Resource::new(0);
    let data = foo.data();

    println!("{data}");

    drop(foo);

    let copy = *data; // Compile Error!!
    println!("{copy}");

    // No double-free in Rust!
    // This function no longer owns foo
    // so it is no longer responsible for
    // free-ing it!
}