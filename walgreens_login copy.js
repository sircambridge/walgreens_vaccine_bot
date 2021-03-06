const puppeteer = require('puppeteer')
const fs = require('fs');


let cookies1 = [
  {
    "name": "akavpau_walgreens",
    "value": "1616539850~id=27927770ef4e41b72fa5a63d57861486",
    "domain": "www.walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 63,
    "httpOnly": false,
    "secure": true,
    "session": true,
    "sameSite": "None",
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "rxvt",
    "value": "1616541345844|1616538274889",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 31,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "bm_sv",
    "value": "56229152670B9F455E0D261B6E6D5B8B~xqUA0xUzLqYpvd5gAVoYbDYkTMqI8Ei/TenhwQS84mKSWyIS7W9flK/rLysXjgvVfL5zPJ2B9BCm+I6ZhUvxtc18jAyfhJXETwCVnEdw4V7Be8rdD2G9Gf1/OJGP4+zfIUDijB25O0fduXVpXCobD88icIwUPMt5UwaFHaP/H4w=",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616539903.121899,
    "size": 210,
    "httpOnly": true,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "mt.mbsh",
    "value": "%7B%22fs%22%3A1616536369079%7D",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616541345,
    "size": 37,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "_gcl_au",
    "value": "1.1.1897946098.1616492412",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1624315545,
    "size": 32,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "IM_throttle_1223",
    "value": "off",
    "domain": "www.walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 19,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "mt.sc",
    "value": "%7B%22i%22%3A1616536365859%2C%22d%22%3A%5B%5D%7D",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616541345,
    "size": 53,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "dtSa",
    "value": "-",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 5,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "mbox",
    "value": "PC#550f7f0f84454760ae6205e09a62dec9.35_0#1679784346|session#462a1a8ba6e74bd8bbfb2bcf5f100153#1616540138",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1679784346,
    "size": 107,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "mt.v",
    "value": "2.1706752528.1616492410767",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1931899545,
    "size": 30,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "jwt",
    "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InYxIn0.eyJleHAiOjE2MTY1NDA0MzEsImlhdCI6MTYxNjUzODYzMSwiaXNzIjoid2FsZ3JlZW5zLmNvbSIsImF1ZCI6ImRvdGNvbSIsImp0aSI6IjFhMWRiM2ZkLTdkNjItNGI4Ni1iM2FlLTE2MWZkY2U1ODYzYSIsInN1YiI6IjIwMDAxNzk1NzE4MSIsImF1dCI6W119.3I5IxuazhHstz4g55zerFpbCXwoC8m1pXLOSQdaduU4",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616625032.264295,
    "size": 295,
    "httpOnly": false,
    "secure": true,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "AMCV_5E16123F5245B2970A490D45%40AdobeOrg",
    "value": "-1124106680%7CMCIDTS%7C18710%7CMCMID%7C23787715520242573430405948494320923994%7CMCAAMLH-1617143078%7C9%7CMCAAMB-1617143078%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1616545478s%7CNONE%7CMCSYNCSOP%7C411-18717%7CvVersion%7C5.2.0%7CMCCIDH%7C1611675534",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1679610278,
    "size": 312,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "dtLatC",
    "value": "514",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 9,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "_uetvid",
    "value": "c38025708bbb11ebb5764524329a5b45",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1617942870,
    "size": 39,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "wag_sid",
    "value": "y0o0iaz878o6bgpsvghwhllo",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616578809,
    "size": 31,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "XSRF-TOKEN",
    "value": "zcvjd0B9O4063Q==.TW/LOx2klMoWXeMVpmuh/LNV1asOWbwLfkzFAwZAKhk=",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 71,
    "httpOnly": true,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "rxVisitor",
    "value": "1616538274887CQ5C6V7O8A3LNNPP2PF301GI85ANLGJU",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 54,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "FirstName",
    "value": "Sabrina",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1648074631.26428,
    "size": 16,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "bm_sz",
    "value": "46F5ED3B5FB4F910CE8FD76B0A1B1C84~YAAQD9scuBuTeEN4AQAAAxAqYQtAqoMyqiVUYv/6/OiVtyCtVmSBjPwQkXaMfFv/Oai+3TrSB0Zqpvrp89MsQ0lcGS+sAwVOrGAARpmykUDsV7S4dGTet196yHZ+QZygW3m5E92d0RCmFOIbpYzfzZpYynXPscOlfEia40YGcYu4pA59g2z9RkBtYvB+ohUAiiv1",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616552250.058109,
    "size": 234,
    "httpOnly": true,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "3s",
    "value": "xJfEq8SeecSyw6DDkMWLWirDhz0=",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1648074631.264241,
    "size": 30,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "profileId",
    "value": "200017957181",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 21,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "2fa",
    "value": "071c90bd873203da07e0796f5709901c",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1648074631.264315,
    "size": 35,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "ak_bmsc",
    "value": "20591210016911D93993044E91DF308C17C5330465290000DE545A60B952E85B~plZeT4ygj1uH4JA0kpW5olnbHefUtsKKFFo/JmOsTY3CtQn7+Ciep3hu+vtUTY0E/p/Q/yYG5hg6lwg0ZfYZYYA1ZNeUSY0/U60pjNTJ8DPj3XRQ0eOgCtYJHMtNl01JdkygaE5jd1B/TwQQSn2O5vlMdKbUnr/Sjp133CLoYflGZwFsdGChVj8Mr/uVxQ3WAhezuybQPA4ZeDBoywp3pTZWs3F3fMEgE1Xx+/37U1/QsodLWge5IhydhMJQNvO4DNbg6VaVIYQpTbSjE2tDt2MzLJ0K0X+lFg/mGWkNUd1C0=",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616539903.114617,
    "size": 374,
    "httpOnly": true,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "dtPC",
    "value": "2$139545827_829h-vDHDOEFCWSDVMUHPMKVMCHFKFHAVRDCFT-0e44",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 59,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "at_check",
    "value": "true",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 12,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "uts",
    "value": "1616538277844",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 16,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "dtCookie",
    "value": "2$PE283035GD2A5DHKIG0OT0NJDAFQQSA9|0eed2717dafcc06d|1",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 61,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "s_sq",
    "value": "%5B%5BB%5D%5D",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 17,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "gRxAlDis",
    "value": "N",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 9,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "AMCVS_5E16123F5245B2970A490D45%40AdobeOrg",
    "value": "1",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 42,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "session_id",
    "value": "ae6a7951-e01e-4cb1-bf94-dddd476c7240",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 46,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "_uetsid",
    "value": "c37fd7f08bbb11ebbf6071526c72ba30",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1616625270,
    "size": 39,
    "httpOnly": false,
    "secure": false,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "s_cc",
    "value": "true",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": -1,
    "size": 8,
    "httpOnly": false,
    "secure": false,
    "session": true,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  },
  {
    "name": "_abck",
    "value": "44BF13BA08881EC4E7127A30C5C130A0~0~YAAQFzPFF9MqokZ4AQAAugw2YQWmDB333/LcGbym4fJe/b4klXr2D6FIDvYM1dAcFFAX+zF+QFpbG7zdt4H9rmUb1DTlvFVK6QCvcwhkMgIh4h3I8etQMp0KDHnsrL32bN7iHWRcxVi1kHbJXRi0nbqW+FqFrS7DeS4qFYlqMdJ/lif6irLoIeCmYAVBIysuSv0bJiRPZWFhm+ZCXLgPtCjZavfqkQbRDHEV862j7lYGNwk0UFyui5V/36tian290MCSvlrp9N6mpp5enKlGG0kK6fPkF8zP8d9WndYbEA6iDY9LjzthdYv20bd9xYK1xyF2erE4zVMTLf+xOkQ9qZMWGVdlFgp6HetGuzUtWUtJ29BETrVuWf8/4fOQIqzofImJlDJWqXGkBXIOCk0bQWxGAIdMME+Hqp/B~-1~||-1||~-1",
    "domain": ".walgreens.com",
    "path": "/",
    "expires": 1648074635.650297,
    "size": 473,
    "httpOnly": false,
    "secure": true,
    "session": false,
    "sameParty": false,
    "sourceScheme": "Secure",
    "sourcePort": 443
  }
]

let browser = null;
let page = null;
async function login(params) {
  console.log(__dirname +'/tmp3');
  if(process.cwd().includes('GitHub')){
    browser = await puppeteer.launch({ 
      headless: false,
      userDataDir:'tmp3'
      // userDataDir: "C:\\Users\\gene\\AppData\\Local\\Google\\Chrome\\User Data",
      // executablePath:"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    });
  }else{
    browser = await chromium.puppeteer.launch({
      args: chromium.args,
      defaultViewport: chromium.defaultViewport,
      executablePath: await chromium.executablePath,
      headless: chromium.headless,
      ignoreHTTPSErrors: true,
    });
  }

  const pages = await browser.pages();


  page = pages[0];

  // const cookies = JSON.parse(await fs.readFileSync('./cookies.json'));
  await page.setCookie(...cookies1);
  await page.setViewport({ width: 1000, height: 1000 });
//   await page.setRequestInterception(true);
//   page.on('request', async (req) => {
//     if(req.url().includes("code=member")){
//       console.log(req.method(),req.url());
//     }
//     req.continue();
//   });
  await page.goto("https://www.walgreens.com/", { waitUntil: 'networkidle2' })
  await page.goto("https://www.walgreens.com/login.jsp", { waitUntil: 'networkidle2' })
  try {
    await page.waitForSelector("#user_name", { timeout: 5000 })
    const input = await page.$('#user_name');
    await input.click({ clickCount: 3 })
    await input.type("sabrina.cambridge@gmail.com");
    const input2 = await page.$('#user_password');
    await input2.click({ clickCount: 3 })
    await page.type('#user_password', 'd3vl0per');
    await page.click("#submit_btn")
    // #page-content > div:nth-child(2) > div.login-page-bg.color__neutral.pb10 > div > div > div > div:nth-child(1) > div > div
    await page.waitForNavigation({waitUntil : "domcontentloaded"})
  } catch (error) {
    console.log("The element didn't appear.")
  }

//   https://www.walgreens.com/login.jsp
  
  let cookies = await page.cookies('https://www.walgreens.com')
  if(process.cwd().includes('GitHub')){
    fs.writeFileSync('cookies.json', JSON.stringify(cookies, null, 2));
  }
  
  console.log(cookies)
  await page.close()
  await browser.close();
  return cookies;
}

if(process.cwd().includes('GitHub')){
  (async function go(){
      await login()
  })()
}else{
  const chromium = require('chrome-aws-lambda');
}


// const chromium = require('chrome-aws-lambda');

exports.handler = async (event, context, callback) => {
  let result = await login()
  return callback(null, result);
};