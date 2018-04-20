from pprint import pprint

def print_dst():
    sh_dir = '/minos/app/junting/transition/Bravo0720/shFiles'
    sh_filenames = []
    with open('{}/subNoOsc.sh'.format(sh_dir)) as f_local:
        for row in f_local.readlines():
            row = row.strip()
            if len(row) > 1:
                sh_filename = row.split(' ')[-1]
                sh_filenames.append(sh_filename)

    sh_filename = sh_filenames[0]
    dsts = []

    for sh_filename in sh_filenames:
        dst_count = 0
        with open('{}/{}'.format(sh_dir, sh_filename)) as f_sh:
            for row in f_sh.readlines():
                if '/minos/data/analysis/NuMuBar' in row and not row.startswith('#'):
                    row = row.strip().split(' ')
                    dst = row[1]
                    dsts.append(dst)
                    dst_count += 1
        print('sh_filename = {}'.format(sh_filename))
        print('dst_count = {}'.format(dst_count))

    print('len(sh_filenames) = {}'.format(len(sh_filenames)))
    print('len(dsts) = {}'.format(len(dsts)))

    pprint(sh_filenames)
    pprint(dsts)

print_dst()
