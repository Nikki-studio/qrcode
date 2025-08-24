/**
 * Main JavaScript file
*/
async function pasteFromClipboard()
{
    try 
    {
        document.getElementById('url').value = await navigator.clipboard.readText();
    } catch (err) 
    {
        console.error('Failed to read clipboard contents: ', err);
    }
}

window.focus = pasteFromClipboard;
window.onpagerevealed = pasteFromClipboard;


