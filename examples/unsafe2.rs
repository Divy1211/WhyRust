fn main() {
    let mut v = vec![10, 20, 30];
    let num1 = &mut v[0];
    let num2 = &mut v[1]; // Compile Error
    let num3 = &v[2]; // Compile Error

    *num1 += 10;
    *num2 += 20;

    println!("{}, {}, {}", num1, num2, num3);
}