# Disable password complexity requirements
SeSecPwdComp -PasswordComplexity 0

# Disable SMBv1 client driver
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart

# Prompt for a restart to apply changes
$restartRequired = Read-Host "Changes have been made. Do you want to restart now? (Y/N)"

if ($restartRequired -eq "Y" -or $restartRequired -eq "y") {
    Restart-Computer -Force
} else {
    Write-Host "Please restart the computer to apply the changes."
}