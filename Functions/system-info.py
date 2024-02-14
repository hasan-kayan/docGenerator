import platform # Python standard library for system information

def analyze_system_information():
    # Get OS and version
    os_system = platform.system()
    os_version = platform.version()

    # Get system information
    system_information = platform.uname()

    # Get hardware information
    hardware_information = {
        "Processor": platform.processor(),
        "Machine": platform.machine(),
        "Node": platform.node(),
        "Architecture": platform.architecture(),
    }

    # Display the information
    print("OS and Version:")
    print(f"OS: {os_system}")
    print(f"Version: {os_version}")
    print("\nSystem Information:")
    print(f"System: {system_information.system}")
    print(f"Node Name: {system_information.node}")
    print(f"Release: {system_information.release}")
    print(f"Version: {system_information.version}")
    print(f"Machine: {system_information.machine}")
    print(f"Processor: {system_information.processor}")

    print("\nHardware Information:")
    for key, value in hardware_information.items():
        print(f"{key}: {value}")

# Test the function
if __name__ == "__main__":
    analyze_system_information()
