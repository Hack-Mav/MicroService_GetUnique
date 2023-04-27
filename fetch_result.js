const fetch = require("node-fetch");

async function JSONData() {
    const response = fetch('http://127.0.0.1:5000/count_words', {
                                    method: 'POST',
                                    headers: {
                                            'Content-Type': 'application/json'
                                    },
                                    body: JSON.stringify({
                                            // url: 'https://en.wikipedia.org/wiki/Python_(programming_language)'
                                            url: 'https://ollivere.co/'
                                    })
                            }).then(response => response.json())
      .then(data => console.log(data));

    console.log(response);
  }

  JSONData();