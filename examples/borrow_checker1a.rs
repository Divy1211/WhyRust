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
