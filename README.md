# tkRecovery

tkRecovery is a work-in-progress macOS program written with python (tkinter) to enter and exit recovery mode on iOS devices with ease. This is designed to easily re-install iOS with Finder and/or help you with the jailbreak process.

# Usage

Connect your iDevice to your Mac and choose "Enter recovery" to start the process.
Once you want to exit from recovery, just click on "Exit recovery".

# Requirements

- Mac device
- MacPorts (for installation)
- libimobiledevice (for the tool to work)

# Installation

### MacPorts: 

To install tkRecovery, you first need to install Apple's Command Line Developer Tools with `xcode-select --install`
Then, install MacPorts for your version of the Mac operating system:
- [Ventura (13)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-13-Ventura.pkg)
- [Monterey (12)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-12-Monterey.pkg)
- [Big Sur (11)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-11-BigSur.pkg)
- [Catalina (10.15)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-10.15-Catalina.pkg)
- [Older OS? See here.](https://www.macports.org/install.php#installing)

### libimobiledevice:

Now that you installed MacPorts, you are now able to install libimobiledevice (what makes the app enter/exit recovery). To start off, type `sudo port install libimobiledevice`. This will start the installation of libimobiledevice.

### tkRecovery itself

Currently there are no downloads. You can check on this page later on or you can [join the Discord](https://discord.gg/vE3sJaWhgF) to be updated on progress.
