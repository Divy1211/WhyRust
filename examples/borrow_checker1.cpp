#include <iostream>


class Resource {
private:
    int* data;

public:
    Resource(int data) {
        this->data = new int;
        *this->data = data;
    }
    ~Resource() {
        delete this->data;
    }

    const int* getData() const {
        return this->data;
    }
};

int main() {
    const Resource foo {0};
    const int* data = foo.getData();
    std::cout << *data << "\n";

    foo.~Resource(); // very obscure

    const int copy = *data; // UB !!
    std::cout << copy  << "\n";

    // Note: foo.~Resource(); is also
    // automatically called here, which is
    // actually a double-free, UB yet again!
}