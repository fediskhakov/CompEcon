
def obj_explore(obj,what='all'):
    '''Lists attributes and methods of a class
    Input arguments: obj = variable to explore,
                     what = string with any combination of
                            all, public, private, methods, properties
    '''
    import sys # this function will run rarely, so import here
    trstr = lambda s: s[:30] if isinstance(s, str) else s  # truncates if string
    spacer = lambda s: " "*max(15-len(s),2)  # returns spacer to pad strings
    hr='-'*60  # horizontal line
    print(obj)  # string representation of the input
    print('%s\nObject report on object = %r' % (hr,obj))
    cl=type(obj)
    print('Objec class     : %s' % cl)
    print('Parent classes  : %r' % cl.__bases__)
    print('Occupied memory : %d bytes' % sys.getsizeof(obj))
    if what in 'all public properties':
        print('PUBLIC PROPERTIES')
        data = [(name,getattr(obj,name)) for name in dir(obj) if not callable(getattr(obj,name)) and name[0:2]!='__']
        for item in data:
            print('%s = %r %s' % (item[0]+spacer(item[0]),trstr(item[1]),type(item[1])))
    if what in 'all private properties':
        print('PRIVATE PROPERTIES')
        data = [(name,getattr(obj,name)) for name in dir(obj) if not callable(getattr(obj,name)) and name[0:2]=='__']
        for item in data:
            print('%s = %r %s' % (item[0]+spacer(item[0]),trstr(item[1]),type(item[1])))
    if what in 'all public methods':
        print('PUBLIC METHODS')
        data = [(name,getattr(obj,name)) for name in dir(obj) if callable(getattr(obj,name)) and name[0:2]!='__']
        for item in data:
            print('%s %s' % (item[0]+spacer(item[0]),type(item[1])))
    if what in 'all private methods':
        print('PRIVATE METHODS')
        data = [(name,getattr(obj,name)) for name in dir(obj) if callable(getattr(obj,name)) and name[0:2]=='__']
        for item in data:
            print('%s %s' % (item[0]+spacer(item[0]),type(item[1])))
