def data_types():
    int_t=10
    str_t='string'
    float_t=1.908
    bool_t=True
    list_t=['g',0,'hi',89]
    dict_t={"name":"Vlada", "age":23}
    tuple_t= (4,6.2)
    set_t={7,9,3,5}

    types=[type(int_t).__name__, type(str_t).__name__, type(float_t).__name__, type(bool_t).__name__, type(list_t).__name__, type(dict_t).__name__, type(tuple_t).__name__, type(set_t).__name__]
    print('['+', '.join(types)+']')

if __name__ == '__main__':
      data_types()