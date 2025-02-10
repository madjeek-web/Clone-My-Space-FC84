<?php  
// Set headers to accept JSON  
header("Content-Type: application/json");

// Retrieve the JSON data sent by the POST request  
$data = json_decode(file_get_contents("php://input"));

// Check that the data is valid  
if (!isset($data->username) || !isset($data->password)) {
    http_response_code(400); // Bad Request  
    echo json_encode(["message" => "Username and password required."]);
    exit();
}

// Simulate a user database  
$users = [
    "user" => "password", // Username and password  
];

// Check if the user exists and if the password is correct  
if (array_key_exists($data->username, $users) && $users[$data->username] === $data->password) {
    // Authentication successful  
    http_response_code(200); // OK  
    echo json_encode(["message" => "Login successful!"]);
} else {
    // Authentication failed  
    http_response_code(401); // Unauthorized  
    echo json_encode(["message" => "Incorrect username or password."]);
}
?>