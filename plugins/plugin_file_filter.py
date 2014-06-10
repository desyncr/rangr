# Compatible with ranger 1.6.*
#
# Filter with smart-case-intivity. If filter is all lowercase
# it performs a insensitive search. Otherwise it applies case-sensitivity.
#

# Save the original filter function
import ranger.container.directory
_accept_file = ranger.container.directory.accept_file

# Define a new one
def custom_accept_file(fname, directory, hidden_filter, name_filter):

    if not name_filter:
        return _accept_file(fname, directory, hidden_filter, name_filter)

    # all lower case is processed as case-insensitive search
    nfilter = name_filter.pattern
    if nfilter.islower():
        fname = fname.lower()

    # Only process filtered input
    if nfilter in fname:
        return True

    return False


# Overwrite the old function
import ranger.container.directory
ranger.container.directory.accept_file = custom_accept_file
