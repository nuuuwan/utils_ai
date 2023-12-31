import os

# Create main folder
os.makedirs('lk_flowers', exist_ok=True)

# Create README.md file
with open('lk_flowers/README.md', 'w') as f:
    f.write(
        "# Sri Lanka Flowers Repository\nThis repository contains data about flowers of Sri Lanka."
    )

# Create LICENSE file
with open('lk_flowers/LICENSE', 'w') as f:
    f.write(
        "MIT License\n\nCopyright (c) 2022 Your Name\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."
    )

# Create sub-folders
os.makedirs('lk_flowers/src', exist_ok=True)
os.makedirs('lk_flowers/tests', exist_ok=True)
os.makedirs('lk_flowers/workflows', exist_ok=True)
