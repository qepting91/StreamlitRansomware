import streamlit as st
from markdownlit import mdlit


def wiki_section():
    st.title("Ransomware: A Comprehensive Overview")
    st.markdown('''
    Ransomware is a form of malicious software that has become one of the biggest cybersecurity problems on the internet today. It encrypts files and documents on individual computers or entire networks, including servers, rendering them inaccessible to the victims. In recent years, ransomware attacks have increased in frequency and sophistication, causing significant financial losses and disruptions to businesses and organizations worldwide.
    ''')

    st.markdown('## Types of Ransomware')
    st.markdown('''
    Ransomware comes in various forms, each with its own characteristics and methods of operation. Some common types of ransomware include:

    - Encrypting Ransomware: This type of ransomware encrypts files and demands a ransom payment in exchange for the decryption key.
    - Screen Lockers: Screen lockers lock the victim's device, preventing access to the operating system or any files until a ransom is paid.
    - Master Boot Record (MBR) Ransomware: MBR ransomware infects the computer's master boot record, making it impossible to boot up the system until a ransom is paid.
    - Mobile Ransomware: Mobile ransomware targets smartphones and tablets, encrypting files or locking the device until a ransom is paid.
    - Fileless Ransomware: Fileless ransomware operates in the computer's memory, making it difficult to detect and remove.
    ''')

    st.markdown('## Usual Targets of Ransomware')
    st.markdown('''
    Ransomware attacks can target a wide range of individuals, businesses, and organizations. Some common targets include:

    - Individuals: Ransomware attacks on individuals can result in the loss of personal files, photos, and other valuable data.
    - Small and Medium-Sized Businesses: Small and medium-sized businesses are often targeted due to their potentially weaker security measures and limited resources for cybersecurity.
    - Large Corporations: Large corporations are attractive targets for ransomware attacks due to the potential for significant financial gain and the potential to disrupt operations.
    - Government Agencies: Ransomware attacks on government agencies can compromise sensitive data and disrupt critical services.
    - Healthcare Organizations: Ransomware attacks on healthcare organizations can have life-threatening consequences, as they may hinder access to patient records and disrupt medical services.
    ''')

    st.markdown('## Reasoning Behind Ransomware Attacks')
    st.markdown('''
    Ransomware attacks are primarily driven by financial motives, but other factors may also come into play. Some common reasons behind ransomware attacks include:

    - Financial Gain: Ransomware attacks are often carried out with the intention of extorting money from victims in exchange for the decryption key.
    - Espionage: In some cases, ransomware attacks may be used as a cover for espionage activities, allowing attackers to gain unauthorized access to sensitive information.
    - Disruption of Operations: Ransomware attacks can disrupt the operations of businesses, organizations, or critical infrastructure, causing significant financial and reputational damage.
    - Revenge: In certain instances, ransomware attacks may be motivated by personal vendettas or a desire to cause harm to specific individuals or organizations.
    - Political Motivations: Ransomware attacks may be politically motivated, targeting government agencies or critical infrastructure to make a political statement or advance a particular agenda.
    ''')

    st.markdown('## Prevention and Mitigation of Ransomware Attacks')
    st.markdown('''
    Preventing and mitigating ransomware attacks requires a multi-layered approach that combines technical measures, employee training, and incident response planning. Some key strategies include:

    - Regular Data Backups: Regularly backing up important data and storing backups offline can help mitigate the impact of a ransomware attack.
    - Use of Anti-Malware Software: Deploying robust anti-malware software can help detect and block ransomware infections.
    - Employee Training and Awareness: Educating employees about the risks of ransomware and how to identify and avoid phishing emails and malicious attachments can significantly reduce the likelihood of successful attacks.
    - Implementation of Security Best Practices: Following security best practices, such as regularly updating software, using strong and unique passwords, and enabling multi-factor authentication, can help prevent ransomware infections.
    - Incident Response Planning: Developing an incident response plan that outlines the steps to be taken in the event of a ransomware attack can help minimize the impact and facilitate a swift recovery.
    ''')

    st.markdown('## Notable Ransomware Attacks')
    st.markdown('''
        Over the years, several high-profile ransomware attacks have made headlines and highlighted the severity of the ransomware threat. Some notable examples include:

        1. WannaCry: The WannaCry ransomware attack in 2017 affected hundreds of thousands of computers worldwide, exploiting a vulnerability in the Windows operating system.
        2. Petya/NotPetya: The Petya/NotPetya ransomware attack in 2017 targeted organizations primarily in Ukraine but quickly spread globally, causing widespread disruption.
        3. Locky: Locky ransomware, first observed in 2016, was one of the most prevalent ransomware families, distributed through malicious email attachments.
        4. CryptoLocker: CryptoLocker, first seen in 2013, was one of the earliest widespread ransomware variants, known for its strong encryption capabilities.
        5. Ryuk: Ryuk ransomware emerged in 2018 and has since been associated with high-profile attacks on organizations, demanding large ransom payments.
        ''')

    st.markdown('## Conclusion')
    st.markdown('''
    Ransomware poses a significant threat to individuals, businesses, and organizations worldwide. Understanding the different types of ransomware, the usual targets, and the motivations behind these attacks is crucial for developing effective prevention and mitigation strategies. By implementing robust security measures, conducting regular employee training, and staying informed about the evolving ransomware landscape, individuals and organizations can better protect themselves against this growing menace.
    ''')

    st.markdown('## References')
    st.markdown('''
    1. [Ransomware: Recent advances, analysis, challenges and ...](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7971931/)
    2. [Microsoft Digital Defense Report OCTOBER 2021](https://www.microsoft.com/security/blog/2021/10/04/microsoft-digital-defense-report-october-2021/)
    3. [CEPOL-European Law Enforcement Research Bulletin](https://www.academia.edu/49851839/CEPOL_European_Law_Enforcement_Research_Bulletin_Europol_2021)
    4. [Ransomware Diaries: Volume 1 - Analyst1](https://www.analyst1.com/wp-content/uploads/2021/10/Volume-1-Analyst1-Ransomware-Diaries.pdf)
    5. [Getting Started Guide and Deep Dive into REvil](https://www.mitre.org/publications/technical-papers/getting-started-guide-and-deep-dive-into-revil)
    6. [What is ransomware? Everything you need to know about one of the biggest menaces on the web | ZDNET](https://www.zdnet.com/article/what-is-ransomware-everything-you-need-to-know-about-one-of-the-biggest-menaces-on-the-web/)
    ''')
