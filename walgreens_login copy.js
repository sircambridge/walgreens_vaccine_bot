const puppeteer = require('puppeteer')
const fs = require('fs');
const chromium = require('chrome-aws-lambda');

let browser = null;
let page = null;
async function login(params) {
  console.log(__dirname +'/tmp3');

  browser = await chromium.puppeteer.launch({
    args: chromium.args,
    defaultViewport: chromium.defaultViewport,
    executablePath: await chromium.executablePath,
    headless: chromium.headless,
    ignoreHTTPSErrors: true,
  });
  const pages = await browser.pages();
  page = pages[0];
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
  fs.writeFileSync('cookies.json', JSON.stringify(cookies, null, 2));
  console.log(cookies)
  await page.close()
  await browser.close();
  return cookies;
}


// (async function go(){
//     await login()
// })()


const chromium = require('chrome-aws-lambda');

exports.handler = async (event, context, callback) => {
  let result = await login()
  // let result = null;
  // let browser = null;

  // try {
  //   browser = await chromium.puppeteer.launch({
  //     args: chromium.args,
  //     defaultViewport: chromium.defaultViewport,
  //     executablePath: await chromium.executablePath,
  //     headless: chromium.headless,
  //     ignoreHTTPSErrors: true,
  //   });

  //   let page = await browser.newPage();

  //   await page.goto(event.url || 'https://example.com');

  //   result = await page.title();
  // } catch (error) {
  //   return callback(error);
  // } finally {
  //   if (browser !== null) {
  //     await browser.close();
  //   }
  // }

  return callback(null, result);
};