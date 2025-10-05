class Example {

private:
    int data1;
    int data2;

public:
    void doSomething1() const {
        /* code */
    }

    void doSomething2() {
        /* code */
    }

    void doSomething3() const {
        /* code */
        delete this;
    }

    void doSomething4() {
        /* code */
        delete this;
    }
}