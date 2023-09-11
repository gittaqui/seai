import streamlit as st
import traceback
from utilities.helper import LLMHelper

def clear_summary():
    st.session_state['summary'] = ""

def get_custom_prompt():
    customtext = st.session_state['customtext']
    customprompt = "{}".format(customtext)
    return customprompt

def customcompletion():
    response = llm_helper.get_completion(get_custom_prompt(), max_tokens=500)
    st.session_state['result'] = response.encode().decode()

try:
    # Set page layout to wide screen and menu item
    menu_items = {
    'Get help': None,
    'Report a bug': None,
    'About': '''
     ## Embeddings App
     Embedding testing application.
    '''
    }
    st.set_page_config(layout="wide", menu_items=menu_items)

    st.markdown("## Bring your own prompt")

    llm_helper = LLMHelper()

    # displaying a box for a custom prompt
    st.session_state['customtext'] = st.text_area(label="Prompt",value='Issue: My Microsoft Teams desktop app stuck in a login loop\nResolution: If you are unable to connect to Teams and Teams keeps on asking you to enter your login credentials, you will need to clear your cached credentials to resolve this issue.\n\nHow To Instructions:\n\n 1. First, close Teams Desktop.\n 2. Next, end all Teams processes in Task Manager using the following steps.\n 3. In Windows, right-click the taskbar.\n 4. Select Task Manager.\n 5. In the Task Manager dialog box, click the Processes tab.\n 6. Under Name, locate and select any Microsoft Teams process.\n 7. Click End Task.\n 8. Repeat the same steps for all Microsoft Teams processes.\n 9. When finished, click Close.\n 10. In the Type Here To Search field, enter Credential Manager.\n 11. Press Enter.\n 12. In the Credential Manager dialog box, click Windows Credentials.\n 13. Locate any line that reads msteams_adalsso/adal_context_x.\n 14. Note that X will be a number.\n 15. To expand the line, click the Expand icon.\n 16. Click the Remove link.\n 17. In the Delete Generic Credential confirmation window, click Yes.\n 18. Repeat the same process for all msteams lines.\n 19. When finished, click Close.\n 20. Launch Teams Desktop and enter your login credentials. You should be able to access Teams.\n\nIssue: Windows Search is Working but Outlook Search is Not\nResolution: If Windows Search is working and you are still experiencing issues with Outlook Search, perform these troubleshooting steps:\n 2. * Verify how many PST files are being viewed during a search.\n    * * A large amount of PST files or a large PST file can cause indexing to take longer than normal.\n    * VERIFY AMOUNT/SIZE OF PST FILES DURING SEARCHES\n    * In Outlook, navigate to Search Options and uncheck everything except your primary Mailbox\n    * Attempt another Outlook search\n 3. If the issue is not resolved, rebuild the index.\n\nIssue: OneDrive files is deleted, overwritten, corrupted, or infected by malware, you can restore your entire OneDrive to a previous date.\nResolution: If your OneDrive files should get deleted, overwritten, corrupted, or infected by malware, you can restore your entire OneDrive to a previous date.\n\nFiles Restore helps Office 365 subscribers undo all the actions that occurred on both files and folders within the last 30 days.\n\nFollow these steps to restore OneDrive to a previous date.\n\nHow To Instructions:\n\n 1. In the upper-right corner of the OneDrive window, click the Settings icon.\n 2. Select Restore Your OneDrive.\n 3. From the Select A Date drop-down, select a preset time.\n 4. To specify a specific date and time, select Custom Date And Time.\n 5. Click and move the slider to get to a specific timeframe.\n 6. In the list, select the change from which all changes applied before it will be applied.\n 7. Click Restore.\n 8. In the Are You Sure You Want To Restore Your OneDrive confirmation window, click Restore.\n\nOnce you click Restore, all changes applied after the date of the selected change will be rolled back.\n\nIf you change your mind after completing a Restore, you can undo it by running Files Restore again and selecting the restore action you just did.\n\nAdditional Information:\n\nFiles Restore uses Version History and the Recycle Bin to restore OneDrive, so it is subject to the same restrictions as those features. When Version History is turned off, Files Restore cannot restore files to a previous version.\n\nFor information about versioning settings, see Enable and Configure Versioning For a List or Library [https://support.office.com/en-us/article/enable-and-configure-versioning-for-a-list-or-library-1555d642-23ee-446a-990a-bcab618c7a37].\n\nDeleted files cannot be restored after they have been removed from the site collection Recycle Bin, either by manual delete or by emptying the Recycle Bin [https://support.office.com/en-us/article/site-collection-recycle-bin-5fa924ee-16d7-487b-9a0a-021b9062d14b].\n\nIf you upload a file or folder again after deleting it, Files Restore will skip the restore operation for that file or folder.\n\nIf some files or folders cannot be restored, a log file will be generated at the root folder of your OneDrive to capture the errors. The name of the file begins with \"RestoreLog\" followed by an ID. You can share the log file with the support team to troubleshoot any issues that may occur.\n \n Issue:', height=400)
    st.button(label="Test with your own prompt", on_click=customcompletion)
    # displaying the summary
    result = ""
    if 'result' in st.session_state:
        result = st.session_state['result']
    st.text_area(label="OpenAI result", value=result, height=200)

except Exception as e:
    st.error(traceback.format_exc())
