

def forward_slashify(txt):
    """
        Replace back slashes to forward slashes
    """
    return txt.replace('\\\\', '/').replace('\\', '/')


def replaceAllValues(filename_in, filename_out, params):
    """
        Read a config file and replace all the parameters reference in that file with the parameter value
        parameter reference is in format r_PARAMNAME.
    """
    f = open(filename_in,'r')
    filedata = f.read()
    f.close()

    ref_indicator = "r_{}"
    for param in params:
        old_data = ref_indicator.format(param)
        new_data = str(params[param])
        filedata = filedata.replace(old_data, new_data)

    f = open(filename_out,'w')
    f.write(filedata)
    f.close()