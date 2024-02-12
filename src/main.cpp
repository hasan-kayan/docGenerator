#include <iostream>
#include <string>

#include "DocumentationGenerator.h" // Include the header file for your DocumentationGenerator class

int main(int argc, char* argv[]) {
    // Check if the user provided the command-line arguments correctly
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <command> [options]" << std::endl;
        return 1;
    }

    // Get the command from the command-line arguments
    std::string command = argv[1];

    // Initialize your DocumentationGenerator object
    DocumentationGenerator docGenerator;

    // Perform actions based on the command
    if (command == "generate") {
        // Handle the "generate" command
        // You can add more options and arguments as needed
        // For example: ./your_app generate --output-dir=output_folder
        // Here you would call the appropriate method/function of your DocumentationGenerator object
        docGenerator.generateDocumentation(/* Pass any necessary arguments */);
    } else if (command == "help") {
        // Handle the "help" command
        // Provide information on how to use the application
        std::cout << "Help information..." << std::endl;
    } else {
        // Handle unknown command
        std::cerr << "Unknown command: " << command << std::endl;
        return 1;
    }

    return 0;
}
