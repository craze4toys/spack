# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rsem(MakefilePackage):
    """RSEM is a software package for estimating gene and isoform expression
       levels from RNA-Seq data."""

    homepage = "http://deweylab.github.io/RSEM/"
    url      = "https://github.com/deweylab/RSEM/archive/v1.3.0.tar.gz"

    version('1.3.0', '273fd755e23d349cc38a079b81bb03b6')

    depends_on('r', type=('build', 'run'))
    depends_on('perl', type=('build', 'run'))
    depends_on('python', type=('build', 'run'))
    depends_on('bowtie')
    depends_on('bowtie2')
    depends_on('star')

    def install(self, spec, prefix):
        make('install', 'DESTDIR=%s' % prefix, 'prefix=')
