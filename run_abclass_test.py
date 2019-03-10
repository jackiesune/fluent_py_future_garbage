#run_abclass_test.py


from abstractclass_TDD import Baseab,Obaseab
import fromabsclass
import  doctest


TEST_FILE='abclass_test.py'
TEST_MSG='{0:14} {1.attempted:2} tests,{1.failed:2} failed-{2}'

def main(argv):
    verbose='-v' in argv
    real_subclass=Baseab.__subclasses__()
    re_subclass=list(Baseab._abc_registry)

    for cls in real_subclass + re_subclass:
        test(cls,verbose)


def test(cls,verbose=False):
    res=doctest.testfile(
        TEST_FILE,
        globs={'ConcreteB':cls},
        verbose=verbose,
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
    tag='FAIL' if res.failed else 'ok'
    print(TEST_MSG.format(cls.__name__,res,tag))


if __name__=='__main__':
    import sys
    main(sys.argv)
