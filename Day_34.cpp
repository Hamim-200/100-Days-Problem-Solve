// class TimeMap {
// private:
//     unordered_map<string, map<int, string>> maps;

// public:
//     TimeMap() {
//         maps = unordered_map<string, map<int,string>>();
        
//     }
    
//     void set(string key, string value, int timestamp) {
//         maps[key][timestamp] = value;
//     }
    
//     string get(string key, int timestamp) {
//         string ans = "";
//         if ((maps.find(key) != maps.end()) && (!maps[key].empty()) && (maps[key].begin())->first<=timestamp){
//             for (auto it = maps[key].rbegin(); it != maps[key].rend(); it++) {
//                 if(it->first <= timestamp) {
//                     ans = it->second;
//                     break;
//                 }
//             }
//         }
//         return ans;
//     }
// };