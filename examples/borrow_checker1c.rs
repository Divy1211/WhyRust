struct Resource {
    data: Box<i32>,
}

impl Resource {
    fn new(data: i32) -> Self {
        Self { data: Box::new(data) }
    }

    fn data_tuple<'a, 'b>(&'a self, other: &'b Resource) -> (&'a i32, &'b i32) {
        (&self.data, &other.data)
    }
}
