// First Swift Code
// Designed by Chulhyun Park 

import Foundation

let path = "/Users/ericpark/Desktop/Bible Project/bible/FinalBibleStandard4.csv"

do {
    // Use contentsOfFile overload.
    // ... Specify ASCII encoding.
    // ... Ignore errors.
    var data = try NSString(contentsOfFile: path,
        encoding: String.Encoding.utf8.rawValue)

    // If a value was returned, print it.
    print(data)
}