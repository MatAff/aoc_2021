
#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>

using namespace std;


int main() {

    // Initialize map to track counts
    map<string, int> my_map = {};

    // Track overlapping points
    int total = 0;

    // Loop through lines
    string line;
    ifstream myfile ("day_05.txt");
    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            std::cout << line << " ";

            // Split
            vector<int> parts;

            // Split middle
            int pos = line.find(" -> ");
            string first = line.substr(0, pos);
            string second = line.substr(pos + 4);

            // Add fist coordinates
            int first_pos = first.find(",");
            parts.push_back(atoi(first.substr(0, first_pos).c_str()));
            parts.push_back(atoi(first.substr(first_pos + 1).c_str()));

            // Add second coordinates
            int second_pos = second.find(",");
            parts.push_back(atoi(second.substr(0, second_pos).c_str()));
            parts.push_back(atoi(second.substr(second_pos + 1).c_str()));

            int x_min = min(parts[0], parts[2]);
            int x_max = max(parts[0], parts[2]);
            int y_min = min(parts[1], parts[3]);
            int y_max = max(parts[1], parts[3]);

            int x_start = parts[0];
            int x_end = parts[2];
            int y_start = parts[1];
            int y_end = parts[3];

            cout << x_min << " " << x_max << " " << y_min << " " << y_max << " ";

            // Condition for hor and vert lines only
            if (x_min==x_max)
            {

                for (int y=y_min; y<=y_max; y++) {
                    int x = x_min;
                    
                    // Update map
                    my_map[to_string(x*1000 + y)]++;
                    cout << " " << to_string(x*1000 + y) << " " << my_map[to_string(x*1000 + y)] << " ";

                    // Update total
                    if (my_map[to_string(x*1000 + y)] == 2)
                    {
                        total++;
                    }

                }

            }
            else {
                if (y_min==y_max)
                {

                    for (int x=x_min; x<=x_max; x++) {
                        int y = y_min;
                        
                        // Update map
                        my_map[to_string(x*1000 + y)]++;
                        cout << " " << to_string(x*1000 + y) << " " << my_map[to_string(x*1000 + y)];

                        // Update total
                        if (my_map[to_string(x*1000 + y)] == 2)
                        {
                            total++;
                        }

                    }

                }
                else 
                {

                    if ((x_min!=x_max) && (y_min!=y_max))
                    {
                        int x_dir = (x_end - x_start) / abs(x_end - x_start);
                        int y_dir = (y_end - y_start) / abs(y_end - y_start);
                        cout << "diag" << " ";
                        for (int x=x_start, y=y_start; ; x = x + x_dir, y = y + y_dir) {

                            if (x > x_max)
                            {
                                cout << "fail";
                                return 1;
                            }

                            if (y > y_max)
                            {
                                cout << "fail";
                                return 1;
                            }

                            // Update map
                            my_map[to_string(x*1000 + y)]++;
                            cout << " " << to_string(x*1000 + y) << " " << my_map[to_string(x*1000 + y)];

                            // Update total
                            if (my_map[to_string(x*1000 + y)] == 2)
                            {
                                total++;
                            }

                            if (x == x_end) 
                            {
                                break;
                            }

                        }

                    }

                }
            }


            cout << endl;

        }
        myfile.close();
    }
    else std::cout << "Unable to open file" << endl; 

    cout << total << " total";

    return 0;
}
