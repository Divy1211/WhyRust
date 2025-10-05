fn split_three(
    slice: &mut [i32]
) -> Option<(&mut i32, &mut i32, &i32)> {
    if slice.len() < 3 {
        return None;
    };

    let ptr = slice.as_mut_ptr();
    unsafe {
        Some((
            &mut *ptr,        // Ok inside unsafe
            &mut *ptr.add(1), // Ok inside unsafe
            & *ptr.add(2),    // Ok inside unsafe
        ))
    }
}


fn main() {
    let mut v = vec![10, 20, 30];
    let (num1, num2, num3) = split_three(&mut v)
        .expect("vector has 3 elements");

    *num1 += 10;
    *num2 += 20;

    println!("{}, {}, {}", num1, num2, num3);
}