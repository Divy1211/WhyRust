struct Example {
    num1: i32,
    num2: i32,
    num3: i32,
}


fn main() {
    let mut example = Example {num1: 10, num2: 20, num3: 30};
    let num1 = &mut example.num1;
    let num2 = &mut example.num2;
    let num3 = &example.num3;

    *num1 += 10;
    *num2 += 20;

    println!("{}, {}, {}", num1, num2, num3);
}