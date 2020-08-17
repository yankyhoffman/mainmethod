import atexit
import inspect
import sys


class _MainMethod:
    """Stores and executes the registered program main method."""
    def __init__(self):
        self._method = None
        self._arg = None

        atexit.register(self._main_execution)

    def _main_execution(self):
        """Main method invocation."""

        # Run the method, using the method's return value as the exit code.
        if self._method is not None:
            if self._arg is None:
                sys.exit(self._method())

            sys.exit(self._method(self._arg))

    def _set_method(self, func):
        """Ensure that only one method is registered as the main method."""
        if self._method is not None:
            raise SyntaxError("Can't register more than one `mainmethod`")

        self._method = func

    def __call__(self, func):
        """Define main method."""

        # Check the method signature for any of the following;
        # 1. No arguments.
        # 2. Single argument `argv` (`sys.argv`).
        params = inspect.signature(func).parameters
        if len(params) != 0:
            if len(params) == 1 and next(iter(params)) in ('argv', 'args'):
                self._arg = sys.argv
            else:
                raise SyntaxError('\n'.join((
                    'Invalid main method signature.',
                    'Supported signatures:',
                    '- `method()`',
                    '- `method(argv)` | `method(args)`',
                )))

        self._set_method(func)

        return func


mainmethod = _MainMethod()
