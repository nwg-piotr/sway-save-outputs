# Maintainer: Nathaniel Maia <natemaia10@gmail.com>
# Maintainer: Piotr Miller <nwg.piotr@gmail.com>
# Author: Piotr Miller <nwg.piotr@gmail.com>
pkgname=('archlabs-sway-save-outputs')
pkgver=0.1
pkgrel=1
pkgdesc="script to save current sway outputs configuration to a text file"
arch=('x86_64')
url="https://github.com/nwg-piotr/sway-save-outputs"
license=('MIT')
depends=('python-i3ipc')
makedepends=('python-setuptools' 'python-wheel')
source=("$pkgname-$pkgver.tar.gz::https://github.com/nwg-piotr/sway-save-outputs/archive/v"$pkgver".tar.gz")

md5sums=('606a16586be46d395dcbd13fe78f474d')

package() {
  cd "sway-save-outputs-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
}
