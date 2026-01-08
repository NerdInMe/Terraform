import subprocess
import sys

def install_terraform():
    """
    Automates the installation of Terraform on an Amazon Linux AMI using the 
    official HashiCorp repository method.
    """
    print("Starting Terraform installation on Amazon Linux...")

    try:
        # 1. Install yum-utils (provides yum-config-manager)
        print("Installing yum-utils...")
        subprocess.run(["sudo", "yum", "install", "-y", "yum-utils"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("yum-utils installed successfully.")

        # 2. Add the official HashiCorp Amazon Linux repository
        print("Adding HashiCorp repository...")
        repo_url = "https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo"
        subprocess.run(["sudo", "yum-config-manager", "--add-repo", repo_url], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("HashiCorp repository added.")

        # 3. Install Terraform from the new repository
        print("Installing Terraform...")
        subprocess.run(["sudo", "yum", "-y", "install", "terraform"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Terraform installed successfully.")

        # 4. Verify the installation
        print("Verifying installation...")
        result = subprocess.run(["terraform", "--version"], check=True, capture_output=True, text=True)
        print(f"Terraform installed version: {result.stdout.strip()}")
        print("Installation complete.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during installation: {e.stderr.decode().strip()}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'sudo' or 'yum' command not found. Ensure the script is run in an appropriate environment.")
        sys.exit(1)

if __name__ == "__main__":
    install_terraform()
