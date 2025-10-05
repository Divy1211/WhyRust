fn main() {
    let mut v = vec![1, 2, 3];
    let mut it = v.iter();
    v.push(4); // Compile Error!!
    println!("{:?}", it.next());
}
