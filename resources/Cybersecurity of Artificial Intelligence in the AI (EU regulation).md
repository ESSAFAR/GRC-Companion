<a name="br1"></a> 

ISSN 1831-9424

J RC SCIENCE FOR POLICY REPORT

Cybers ecurity of Art ificia l Int e llige nce in

the AI Act

Guiding principles to address the cybe rs e curit y requirement for high-ris k

AI systems

Junklewitz, H., Ha mon, R., André, A., Eva s, T., Soler

Ga rrido, J., Sanchez Ma rtin, J.

2023

EUR 31643 EN



<a name="br2"></a> 

This publication is a Science for Policy report by the J

service. It aims to provide evidence-based scientific support to the European policymaking process. The contents of this publication do

not necessarily reflect the position or opinion of the European Commission. Neither the European Commission nor any person acting on

behalf of the Commission is responsible for the use that might be made of this publication. For information on the methodology and

quality underlying the data used in this publication for which the source is neither Eurostat nor other Commission services, users should

contact the referenced source. The designations employed and the presentation of material on the maps do not imply the expression of

any opinion whatsoever on the part of the European Union concerning the legal status of any country, territory, city or area or of its

authorities, or concerning the delimitation of its frontiers or boundaries.

Cont a ct information

Name: Ignacio Sanchez

Address: DG Joint Research Centre, Directorate T Digital Transformation and Data, Unit T.2 Cybersecurity and Digital Technologies,

Via Enrico Fermi 2749, 21027 Ispra (VA), Italy

Email: Ignacio.Sanchez@ec.europa.eu

Te l.: +39 033278 5998

EU Science Hu b

https://joint-research-centre.ec.europa.eu

JRC134461

EUR 31643 EN

PDF

ISBN 978-92-68-07045-1

ISSN 1831-9424

doi:10.2760/271009 KJ-NA-31-643-EN-N

Luxembourg: Publications Office of the European Union, 2023

© European Union, 2023

The reuse policy of the European Commission documents is implemented by the Commission Decision 2011/833/EUof 12 December 2011

on the reuse of Commission documents (OJ L 330, 14.12.2011, p. 39). Unless otherwise noted, the reuse of this document is authorised

under the Crea tive Commons Attribut ion 4.0 International (CC BY 4.0) licence [(](https://creativecommons.org/licenses/by/4.0/)<https://creativecommons.org/licenses/by/4.0/>[)](https://creativecommons.org/licenses/by/4.0/). This means

that reuse is allowed provided appropriate credit is given and any changes are indicated.

For any use or reproduction of photos or other material that is not owned by the European Union permission must be sought directly from

the copyright holders.

How to cite this report: Junklewitz, H., Ha mon, R., André, A., Eva s, T., Soler Garrido, J. and Sanchez Ma rtin, J.I., Cybersecurity of Art ificia l

Intelligence in the AI Act, Publications Office of the European Union, Luxembourg, 2023, doi:10.2760/271009, JRC134461.



<a name="br3"></a> 

Cont ent s

[Contents](#br3)[........................................................................................................................................................................................................................................................................I](#br3)

[Abstract](#br4)[ ](#br4)[.......................................................................................................................................................................................................................................................................1](#br4)

[Authors](#br5)[.........................................................................................................................................................................................................................................................................2](#br5)

[Exe](#br6)[ ](#br6)[cut](#br6)[ ](#br6)[ive](#br6)[ ](#br6)[summary](#br6)[..........................................................................................................................................................................................................................................3](#br6)

[1](#br8)

[2](#br9)

[Introduction](#br8)[.....................................................................................................................................................................................................................................................5](#br8)

[Ba](#br9)[ ](#br9)[ckground](#br9)[.....................................................................................................................................................................................................................................................6](#br9)

[2.1](#br9)[ ](#br9)[Ma](#br9)[ ](#br9)[chine](#br9)[ ](#br9)[Learning](#br9)[........................................................................................................................................................................................................................6](#br9)

[2.2](#br9)[ ](#br9)[AI](#br9)[ ](#br9)[Cybe](#br9)[ ](#br9)[rsecurity](#br9)[............................................................................................................................................................................................................................6](#br9)

[2.3](#br10)[ ](#br10)[AI](#br10)[ ](#br10)[Cybersecurity](#br10)[ ](#br10)[in](#br10)[ ](#br10)[the](#br10)[ ](#br10)[AI](#br10)[ ](#br10)[Act](#br10)[...........................................................................................................................................................................................7](#br10)

[2.4](#br10)[ ](#br10)[AI](#br10)[ ](#br10)[Cybersecurity](#br10)[ ](#br10)[Standardisation](#br10)[.................................................................................................................................................................................7](#br10)

[Guiding](#br12)[ ](#br12)[principles](#br12)[ ](#br12)[to](#br12)[ ](#br12)[address](#br12)[ ](#br12)[the](#br12)[ ](#br12)[cybersecurity](#br12)[ ](#br12)[requirement](#br12)[ ](#br12)[of](#br12)[ ](#br12)[the](#br12)[ ](#br12)[AI](#br12)[ ](#br12)[Act](#br12)[ ](#br12)[.....................................................................................9](#br12)

[Guiding](#br12)[ ](#br12)[principle](#br12)[ ](#br12)[1](#br12)[:](#br12)[ ](#br12)[The](#br12)[ ](#br12)[focus](#br12)[ ](#br12)[of](#br12)[ ](#br12)[the](#br12)[ ](#br12)[AI](#br12)[ ](#br12)[Act](#br12)[ ](#br12)[is](#br12)[ ](#br12)[on](#br12)[ ](#br12)[AI](#br12)[ ](#br12)[systems.](#br12)[.................................................................................................................9](#br12)

[Guiding](#br12)[ ](#br12)[principle](#br12)[ ](#br12)[2](#br12)[:](#br12)[ ](#br12)[Complia](#br12)[ ](#br12)[nce](#br12)[ ](#br12)[with](#br12)[ ](#br12)[the](#br12)[ ](#br12)[AI](#br12)[ ](#br12)[Act](#br12)[ ](#br12)[necessarily](#br12)[ ](#br12)[requires](#br12)[ ](#br12)[a](#br12)[ ](#br12)[security](#br12)[ ](#br12)[risk](#br12)[ ](#br12)[assessment.](#br12)[......................9](#br12)

[3](#br12)

[Guiding](#br13)[ ](#br13)[principle](#br13)[ ](#br13)[3](#br13)[:](#br13)[ ](#br13)[Securing](#br13)[ ](#br13)[AI](#br13)[ ](#br13)[systems](#br13)[ ](#br13)[requires](#br13)[ ](#br13)[an](#br13)[ ](#br13)[integrated](#br13)[ ](#br13)[and](#br13)[ ](#br13)[continuous](#br13)[ ](#br13)[approach](#br13)[ ](#br13)[using](#br13)[ ](#br13)[proven](#br13)

[practices](#br13)[ ](#br13)[and](#br13)[ ](#br13)[AI-](#br13)[ ](#br13)[spe](#br13)[ ](#br13)[cific](#br13)[ ](#br13)[controls.](#br13)[.........................................................................................................................................................................................10](#br13)

[Guiding](#br13)[ ](#br13)[principle](#br13)[ ](#br13)[4](#br13)[:](#br13)[ ](#br13)[The](#br13)[ ](#br13)[re](#br13)[ ](#br13)[are](#br13)[ ](#br13)[limits](#br13)[ ](#br13)[in](#br13)[ ](#br13)[the](#br13)[ ](#br13)[state](#br13)[ ](#br13)[of](#br13)[ ](#br13)[the](#br13)[ ](#br13)[art](#br13)[ ](#br13)[for](#br13)[ ](#br13)[securing](#br13)[ ](#br13)[AI](#br13)[ ](#br13)[models.](#br13)[......................................................10](#br13)

[Conclusions](#br15)[ ](#br15)[..................................................................................................................................................................................................................................................12](#br15)

[4](#br15)

[References](#br16)[.............................................................................................................................................................................................................................................................13](#br16)

[Lis](#br18)[ ](#br18)[t](#br18)[ ](#br18)[of](#br18)[ ](#br18)[abbreviations](#br18)[ ](#br18)[....................................................................................................................................................................................................................................15](#br18)

i



<a name="br4"></a> 

Abstract

Th e European Commission proposal for the AI Act represents a significant milestone in the regulation of

Artificia l Intelligence (AI). Th is report focuses on the cybersecurity requirement for high-risk AI systems, as set

out in Art icle 15 of the regulation. It presents a high level analysis in the context of the rapidly evolving AI

landscape, and provides a set of key guiding principles to achieve compliance with the AI Act .

Th e proposed AI Act focuses on AI systems. Th e internal structure of AI systems involves a range of components.

Although AI models are essential components of AI systems, they do not constitute AI systems on their own.

Th e AI Act cybersecurity requirement applies to the AI system as a whole and not directly to its internal

components.

In order to ensure compliance, a security risk assessment should be conducted ta king into account the design

of the system, to identify risks , and implement the necessary mitigation measures. Th is process requires an

integrated and continuous approach using proven cybersecurity practices and procedures combined with AI-

specific controls.

Although the state of the art for securing AI models has limitations, AI systems may still achieve compliance

with the AI Act's cybersecurity requirement as long as their cybersecurity risks are effectively mitigated through

other measures not exclusively deployed at AI model level. Howe ve r, this may not always be possible, and

indeed for some high-risk AI systems using emerging AI technologies, it may not be feasible to achieve

compliance with the cybersecurity requirement of the AI Act unless in their design these system additionally

introduce new cybersecurity controls and mitigation measures of proven effectiveness

1



<a name="br5"></a> 

Aut hors

Junklewitz, He nrik (Joint Research Centre, European Commission)

Ha mon, Rona n (Joint Research Centre, Europea n Commission)

André, Antoine-Alexa ndre (DG CONNECT, European Commission)

Eva s, Tatjana (DG CONNECT, Europea n Commis sion)

Soler Ga rrido, Josep (Joint Resea rch Centre, European Commission)

Sanchez, Igna cio (Joint Resea rch Centre, European Commis sion)

2



<a name="br6"></a> 

Execut ive summary

Th e European Commission proposal for the AI Act represents a significant milestone in the regulation of

Artificia l Intelligence (AI). Th is report focuses on the cybersecurity requirement for high-risk AI systems, as set

out in Art icle 15 of the Commission proposal of the AI Act . It provides a high level a na lysis of the practical

applications of this requirement to AI systems in the context of the rapidly evolving AI landscape, and provides

a set of key guiding principles to achieve compliance with the AI Act .

Background

Th e increased adoption of Artificia l Intelligence represents a paradigm shift in software development. AI enables

solving problems and carrying out tasks that otherwise would be intractable for computers. Artificia l Intelligence

has the potential to revolutionise many sectors and bring substantial benefits to society. Howe ve r, due to the

nature of their underlying technologies, AI also introduces new risks and challenges that need to be properly

addressed.

AI systems are computer systems and, as such, they inherit all the cybersecurity risks already connected to

traditional digital systems that operate in simila r contexts. In addition, the uptake of AI technologies introduces

new cybersecurity risks connected to the emergence of new classes of AI-spe cific vulnerabilities. AI

cybersecurity is an emerging field that a ims to research and address these AI specific vulnerabilities, including

adversarial machine learning attacks, data poisoning or backdoors embedded in AI models.

Th e global AI landscape is evolving rapidly, with new AI techniques being introduced regularly. The current AI

ecosystem is composed of a wide variety of AI models and techniques at various levels of maturity. Aga inst

this background, current cybersecurity practices and procedures, already well established and used to secure

traditional software (and hardware based) systems, are limited in their capacity to address the wider range of

cybersecurity risks of AI systems. The re are ongoing research and operational efforts at global level to better

understand and address these risks extending the current practices and procedures and develop new ones in

order to ensure the cybersecurity of AI systems. These efforts are already resulting in the development of AI

cybersecurity risk management tools and the definition of security controls that are tailored to the particularities

of securing AI systems, including AI cybersecurity metrics and mitigation measures to address AI-s pe cific

vulnerabilities.

Policy context

Th e proposed AI Act represents a significant milestone in the regulation of Artificia l Intelligence. Th is legislation

a ims to establish a horizontal framework for trustworthy AI. At its core, the proposed AI Act is designed to

address risks to health, safety and fundamental rights specifically associated with AI technologies by setting

legally binding requirements for high-risk AI systems. Prior to the deployment on the EU market, a provider of

a high-risk AI a pplication, will have the obligation to adopt the necessary organisational and technical measures

to achieve conformity with the requirements.

In line with a well-established EU system of product safety regulation, harmonised standards are one of the

main means to achieve compliance and conformity with the legislative requirements. European standards will

be developed by Europea n Standardisation Organisations following the standardisation request of the Europea n

Commis sion published on 22 May 2023 and will eventually become harmonised standards at the time of

application of the AI Act . It is important to note that the standardisation request makes clear that the reach of

AI standardisation is determined by the technological maturity of AI technologies, explicitly referring to the

technological state of the art as the basis of standardisation. Therefore, in terms of technical cybersecurity

measures, AI standards are expected to cover mature and generally accepted measures for cybersecurity of AI

systems. Th is anticipates an ongoing need for standardisation work on AI cybersecurity in the coming years.

Howe ve r, this does only imply technological limits for securing individual models, and not a limit to the

development of standards. Instead, an initial set of cybersecurity standards in response to the initial AI Act

standardisation request should provide a strong basis in terms of a va ila ble technical controls for achieving and

measuring AI cybersecurity together with general outcome-based horizontal cybersecurity requirements for

high-risk AI systems.

Guiding principles

these four guiding principles:

3



<a name="br7"></a> 

1\. The focus of the AI Ac t is on AI systems. Th e structure of AI systems involves a range of internal

components, some of which are AI-rela ted, whilst others are not. Alt hough AI models are essential

components of AI systems, they do not constitute AI systems on their own. The cybersecurity

requirement set out by the AI Act applies to the AI system as a whole and not directly to its internal

components.

2\. Complia nce wit h the AI Ac t necessarily requires a security risk assessment. In order to ensure

that an AI system complies with the cybersecurity requirement of the AI Act, a security risk assessment

should be conducted considering the internal architecture of the AI system and the intended application

context. Th is cybersecurity risk assessment, carried out in the context of the Ris k Mana gement System

described in the Art icle 9 of the AI Act , a ims to identify the specific risks, translate the higher level

cybersecurity requirement of the regulation down to specific requirements for the components of the

system and implement the necessary mitigation measures.

3\. Securing AI systems requires an integrated and continuous approach using proven practices

and AI-s pecif ic controls. Th is process should leverage current cybersecurity practices and

procedures, using a combination of existing controls for software systems and AI-model specific

measures. AI systems are the sum of all their components and of their interactions. Aholistic approach

following the security-in-depth and security-by-design principles should be adopted to ensure that AI

systems achieve compliance with the cybersecurity requirement of the AI Act .

4\. There are limits in the state of the art for securing AI models. Awide variety of AI technologies

of different degrees of maturity coexist in the current AI landscape. Not all AI technologies might be

ready for use in AI systems designed to be deployed in high-risk scenarios, unless their limitations in

terms of cybersecurity are properly addressed. In some cases, particularly for emergent AI

technologies, there are inherent limitations that cannot be exclusively addressed at the level of the AI

model. In those cases, compliance with the cybersecurity requirement of the AI Act can only be achieved

following the holistic approach described earlier.

Conclusions

Th e guiding principles la id out in this report are intended to help all relevant stakeholders in addressing the

cybersecurity requirement for high-risk AI systems, as set out in Art icle 15 of the proposal of the European

Commis sion. It is important to understand that limitations in the state of the art for securing AI models e xist

and that harmonised standards developed for the AI Ac t are expected to provide horizontal requirements to

ensure the cybersecurity of AI systems, but not expected to cover approaches lacking maturity beyond the

generally accepted state of the art in AI cybersecurity.

Nonetheless, these technical limitations do not necessarily impede compliance of AI systems with the

cybersecurity requirement of the AI Act . High-ris k AI systems can still achieve compliance if they appropriately

mitigate the overall cybersecurity risks of the system through other complementary measures, following an

integrated approach combining well established cybersecurity practices and procedures with AI specific

measures.

Howe ve r, it is important to acknowledge that this may not a lwa ys be possible and that for some high-risk AI

systems making use of emerging AI technologies, it may not be feasible to achieve compliance with the

cybersecurity requirement of the AI Act using currently existing and mature cybersecurity techniques and

measures, highlighting the need for technological advancements in parallel to standardisation in this area.

4



<a name="br8"></a> 

1

Int roduct ion

Th e EU AI Act (European Commis sion 2021b) represents a significant milestone in the regulation of artificial

intelligence (AI) technologies. Th is legislation a ims to establish a horizontal framework for trustworthy AI

systems that are safe, secure and compliant with Europe a n fundamental rights and values. At its core, the AI

Act is designed to address risks to health, safety and fundamental rights specifically associated with AI

technologies by setting legally binding requirements for high-risk AI systems. Prior to the deployment on the EU

market, a provider of a high-risk AI a pplication must adopt the necessary organisational and technical measures

to achieve conformity with the requirements. Be hind this approach is the intention to build public trust in AI as

a transformative technology and ensure that it benefits the society as a whole. Not e that at the time of

publication the A

original Europea n Commission proposal (European Commission 2021b).

In line with a well-established EU system of product safety regulation (European Parliament and Council of the

Europea n Union 2012), harmonised standards are one of the main means to achieve compliance and conformity

with the legislative requirements. Ha rmonised standards will be developed by Europea n Standardisation

Organisations following a standardisation request of the Europea n Commis sion published in May 2023

(Europea n Commission 2023). It is important to note that the standardisation request makes clear that the

reach of AI standardisation is determined by the technological maturity of AI technologies, explicitly referring

to the state of the art (S OTA) in technology<sup>1</sup> as the basis of standardisation.

AI is a rapidly evolving field, with novel and emergent approaches, models, and tools being introduced on an

increasingly frequent basis (OECD 2023; 2022). Th is pace has dramatically accelerated in recent months driven

by new developments and products on large-scale AI models (Bomma sa ni et al. 2021). In the current AI scientific

ecosystem, a wide variety of techniques and approaches of different levels of maturity coexist. Whils t some AI

models are based on well-established techniques that have been used for decades, many techniques, in

particular those driving the current innovative developments, ha ve only been in use for a few years or even

months. Additionally, research has focused primarily on improving the accuracy of models, and the shift towards

the consideration of trustworthy requirements has only gained momentum over the past few years, in the light

of potential negative consequences of the use of AI in the society (Hig h Level Expe rt Group on Artificia l

Intelligence 2019). Therefore, considerations such as robustness, explainability or cybersecurity of AI models

are often in earlier stages of research and development.

Th is report focusses on the requirement of cybersecurity for high-risk AI systems, as set out in Art icle 15 of the

proposed AI Act . The requirements of cybersecurity, accuracy and robustness, are connected to the technical

dimension of AI systems and require a deep understanding of the inner workings of AI systems, established

technical practices and standards.

Eve n though established standards and practices in cybersecurity may apply to AI systems as they do to other

software systems, AI-s pe cific technological challenges exis t and ha ve not yet been the subject of established

security practices or specific standards. Howe ve r, work is increasingly being dedicated to the topic in form of

reports, studies and first international standardisation work items (Tabassi et al. 2019; Berghoff et al. 2021;

Malatras, Agra fiotis, and Ada mczyk 2021; The MITRE Corpora t ion 2022). Currently, for security engineering

purposes such as the practical implementation of processes and techniques to secure systems, many AI- spe cific

security approaches and tools may not be considered mature enough to be directly used for properly securing

certain AI models individually (Berghoff et al. 2021). The cybersecurity of AI (or AI cybersecurity) is an emerging

field that a ims to fill this gap, and that strongly relies on ongoing research activities in fields such as security

engineering or adversarial machine learning (Papernot et al. 2016). In fact, the main purpose of the AI Act is to

address the AI- spe cific risk in AI technology as discussed in detail in the AI Act impact assessment (European

Commis sion 2021a) - and as such it can be expected that considerations are needed that go beyond established

practice in software security to address its requirements.

In the report, these considerations are elaborated and guidance is provided for standardisation bodies and AI

providers that seek to comply with the cybersecurity requirement of the proposed AI Act . These results are

summarised in four key messages and recommendations. The report is conducted as part of an ongoing

collaboration between the JRC and DG CONNECT, providing scientific and technical support to the development

of the AI Act and related standardisation activities.

<sup>1</sup> Defined as generally accepted practices and not as the latest developments in research.

5



<a name="br9"></a> 

2

Ba ckground

Art icle 3 (1) of the proposed AI Act defines an AI system as (AI system) means software that is developed with

one or more of the techniques and approaches listed in Annex I and can, for a given set of human-defined

objectives, generate outputs such as content, predictions, recommendations, or decisions influencing the

environments they interact with , while Annex I covers both machine learning and other approaches to AI such

as knowledge-based systems. In this report, the analysis is focused on machine learning, as it currently accounts

for the most prominent technical approaches in AI and also poses most of the challenges for AI cybersecurity

relevant for the AI Act .

2\.1 Ma chine Lea rning

Ma chine learning itself is not homogeneous, and different approaches co-exist that have emerged since the

creation of the field. Broadly, the main features of machine learning compared to traditional software can be

summarised in three points: 1) reasoning and learning capabilities, 2) strong reliance on data, and 3) stochastic

nature of outcomes.

Essentially, in machine learning a so-called model is trained from existing data using statistical and optimisation

techniques, which then can be used for a range of reasoning, prediction, decision or generation tasks. For the

purpose of this report, three main categories of machine learning approaches are distinguished, providing a

rough classification into increasingly more complex AI models and approaches, usua lly relying on progressively

larger training data sizes and more computing power:

1\. Tra dit iona l machine learning, processing pre-processed features, e .g., linear regression,

decision trees, Bayesia n network classifiers, or support vector machines, see, for example (Bis hop

2007).

2\. Adva nced machine learning, based on deep learning using neural networks, e .g., deep

convolutional neural networks or recurrent neural networks. See, for example (Goodfellow, Be ngio, and

Courville 2016).

3\. La rge-sca le deep learning systems, such as attention-based large-scale neural networks trained

on very large data sets. See (Bomma sa ni et al. 2021).

2\.2 AI Cybersecurit y

AI cybersecurity is an emerging field of study, collecting and combining knowledge and approaches from

different fields such as AI research, adversarial machine learning and general cybersecurity. Different angles

can be considered in the interaction between these fields, most prominently the application of AI to enhance

and reinforce cybersecurity, the misuse of AI systems for malicious purposes, and the cybersecurity of AI

systems. In the context of this report, only the latter is considered.

For the purposes of cybersecurity, AI can be viewed as a type of software and, thus, a goal of the field is to rely

on already established practices where possible. Howe ve r, a range of AI- spe cific technological challenges e xist

for AI cybersecurity, and neither many tested security practices nor specific standards have been introduced yet

to address them (Papernot et al. 2016). These challenges are mostly connected to newly introduced computing

and product lifecycle paradigms by machine learning systems and due to the fact that a growing number of

new AI-s pe cific vulnerabilities are being identified for machine learning systems, such as evasion attacks, data

poisoning, model stealing, model inversion, or backdoors embedded in models (Berghoff et al. 2021; Malatras,

Agra fiotis, and Ada mczyk 2021). The MITRE corporation (Th e MITRE Corpora t ion 2022) provides an especially

useful, continuously updated and developed taxonomy and kill chain analysis about such AI- specific attacks.

Cha llenges for AI Cybersecurity can be roughly grouped into two categories:

1\. Organisational challenges related to processes, e.g. harmonising terminologies, threat taxonomies, and

definitions across fields and standards; managing AI lifecycle security and AI-s pecific supply chain

security problems; adapting existing security controls for AI software.

2\. Resea rch and Development challenges related to techniques, e.g. assessment of attacks on machine

learning models; developing AI-s pe cific security measures and hardening models for more advanced

AI methodologies; defining metrics and measures for AI cybersecurity and adversarial robustness of AI

models; evaluating trade-offs with other requirements such as between accuracy and cybersecurity;

developing practical AI threat modelling experience.

6



<a name="br10"></a> 

Cybersecurity is largely focusing on risk-based approaches, and, as with any novel technology, AI should be

appreciated in the light of a trade-off between opportunities and challenges (Na i Fovino et al. 2020). It remains

clear that the risks for many of the listed challenges need to be carefully assessed, as well as whether they

can be addressed directly. Howeve r, cybersecurity has a long history of securing new technologies under new

risks and many proven practices will be applicable in this case too, such as organising the cybersecurity of a

software systems in such a way that insecure systems are encapsulated in several layers, with outer security

controls like access management

-in-

principle) (Cha pple, Stewart, and Gibs on 2021).

2\.3 AI Cybersecurit y in the AI Ac t

AI cybersecurity is covered in the AI Act in Art icle 15, albeit not as an individual requirement, but together with

accuracy and robustness. In addition, the cybersecurity requirement is further explained in Recita l 51. Building

on Art icle 15 and Recita l 51, the standardisation request, Annex II (2 .8 ), provides further operational details on

the cybersecurity requirement. As summarised by the JRC (Soler Ga rrido et al. 2023), operationally, the

cybersecurity requirement includes four main elements:

●

High- ris k AI systems should be ensured and designed to be resilient against attempts to alter their

use, behaviour, and performance and to compromise their security properties by malicious third

●

●

●

Organisational and technical solutions shall be implemented to address these goals.

Acybersecurity risk assessment shall be done for high-risk AI systems.

Te chnica l solutions shall be appropriate to the relevant circumstances and risks .

After the AI Act becomes applicable all high-risk AI systems as defined by the legislation would ha ve to undergo

a conformity assessment and comply with the cybersecurity requirement before they can be used or put into

service in the EU market.

The re are two main possibilities to ensure conformity. One option is compliance with harmonised standards as

la id down in Cha pter 5 of the AI Act . Recita l 61 and Art icle 40 state how harmonised standards can provide a

presumption of conformity with the requirements of the legislation.

Ha rmonised standards are however a lwa ys voluntary and the provider of an AI system can a lwa ys demonstrate

a conformity with the requirements of AI Act without relying on harmonised standards, which provides a second

option to ensure conformity. It should be noted however that according to the Europea n Commis sion 2022

and

and the goal should be that harmonised standards will

remain the main means of showing compliance also in case of the AI Act .

2\.4 AI Cybersecurit y St a nda rdisa t ion

In compliance with regulation (EU) No 1025/2012 on European standardisation (Europea n Parliament and

Council of the European Union 2012) and with the new standardisation strategy of the Europea n Commis sion

(Europea n Commission 2022a), the AI Act foresees in Recita l 61 that standardisation should play a key role to

provide technical solutions to providers to ensure compliance with this Regula tion . Th e first AI standardisation

request published by the Europea n Commission in May 2023 provides a formal mandate to develop the

standards required in support of the future AI regulation.

Th e standardisation request sets the level of expectations related to the AI Act requirements, including on

cybersecurity. In addition, it explicitly acknowledges that standards should be developed considering the state

of the art (S OTA) in technology. In addition to the central reference to the AI Act , for cybersecurity, the AI

standardisation request also refers to the proposed Cybe r Re s ilie nce Act (CRA) (European Commis sion 2022b).

Europea n standardisation deliverables shall take due account of the essential requirements for products with

digital elements as listed in Sections 1 and 2 of Annex I in the CRA. If an AI system fa lls under the scope of

both CRA and AI Act , and if it fulfils the essential requirements of the CRA, it should be deemed compliant with

the cybersecurity requirement in Art icle 15 of the AI Act (see Recita l 29, CRA). In this case, the main arguments

of this paper can be considered equally applicable, since a lso the CRA requests a risk-based approach to the

cybersecurity of systems.

7



<a name="br11"></a> 

Th e standardisation request is addressed to CEN-CENELEC (European Committee for Standardization and

Europea n Committee for Electrotechnical Standardization), with a requirement to consult ETSI (European

Telecommunications Standards Institute) in specific areas of standardisation, such as, notably, in cybersecurity.

It is important to note that the standardisation request makes clear that the reach of AI standardisation is

determined by the technological maturity of AI technologies, explicitly referring to the technological state of the

art as the basis of standardisation. Therefore, in terms of technical cybersecurity measures, AI standards are

expected to cover mature and generally accepted measures for cybersecurity of AI systems. Th is anticipates an

ongoing need for standardisation work on AI cybersecurity in the coming years. Howe ve r, this does only imply

technological limits for securing individual models, and not a limit to the development of standards. Instead, an

initial set of cybersecurity standards in response to the initial AI Act standardisation request should provide a

strong basis in terms of a va ila ble technical controls for achieving and measuring AI cybersecurity together with

general outcome-based horizontal cybersecurity requirements for high-risk AI systems. Recently, the JRC

published an analysis of the preliminary AI standardisation work plan in support of the AI Act (Soler Ga rrido et

al. 2023) and these considerations regarding cybersecurity were summarised as follows:

●

Ma ny non-AI-s pecific security measures can largely be taken from the ISO 27000 series, which

includes well established procedures on organisational principles, risk management and security

controls. Howe ve r, current existing standards are not yet adapted to be used for AI software.

●

Standards on AI-spe cific cybersecurity are beginning to be developed on the international level,

but are not yet a va ila ble, most notably ISO 27090 on AI- s pecific mitigation and controls. Work at

Europea n level is just beginning, and may cover AI cybersecurity elements in dedicated standards

on risk and trustworthiness.

8



<a name="br12"></a> 

3

Guiding principles to address the cybersecurity requirement of t he AI

Act

Th is section presents four guiding principles to facilitate the understanding and compliance with the

cybersecurity requirement of the AI Act . These guiding principles are developed in the policy context of the AI

Act and its standardisation, and are based on the analysis of the current state of play in AI cybersecurity and

on established cybersecurity principles.

Cybersecurity is a field that has gained a lot of experience with the advent of new computing paradigms such

as cloud computing, Internet of Things (IoT) and edge systems, and it is now evolving to address the risks

brought by the uptake of AI technologies.

Guiding principle 1: The focus of the AI Ac t is on AI systems.

As stated in its Art icle 1, the AI Act la ys down specific requirements for high-risk AI systems. These requirements,

including the one on cybersecurity, apply to the high-risk AI system, and not directly to the AI models (or any

other internal system component) contained within it.

An AI system, formally defined in Art icle 3(1 ), should be understood as a software that includes one or several

AI models as key components alongside other types of internal components such as interfaces, sensors,

databases, network communication components, computing units, pre-processing software, or monitoring

systems.

Although AI models are essential components of AI systems, they do not constitute AI systems on their own, as

they will a lwa ys require other software components to be able to function and interact with users and the

virtual or physical environment. The cybersecurity requirement of the AI Act does not apply directly the internal

components of the systems (such as the AI models), but instead to the AI system as a whole. For example, an

AI-based computer vision system does not only include the AI model, but also the sensors and software

components to pre-process and manipulate inputs and outputs. Similarly, an AI chatbot may rely on large

language models, but also on a traditional cloud infrastructure to be accessed through the internet and manage

the hardware required to run the application.

Th is perspective is aligned with known approaches in cybersecurity, where the system-level view is often applied

when considering the security of complex software systems with concepts such as security-in-depth, applying

security controls at different layers of an ICT system (Cha pple, Stewart, and Gibs on 2021), and top-down threat

modelling from the system to its components (Shostack 2014).

Guiding principle 2: Complia nce wit h the AI Ac t necessarily requires a security risk

assessment.

In order to ensure the compliance of a high-risk AI system to the AI Act , the cybersecurity requirement needs to

be mapped from the system to individual components in the context of the Ris k Management System described

in Art icle 9. Practically speaking, this involves a cybersecurity risk assessment of the system and its components

(Ros s 2012). In particular, for the risk assessment, AI models shall be considered by ta king into account their

limitations and vulnerabilities in the context of their interactions with other non-AI components of the system.

Th is risk-based approach is crucial to determine the details of a cybersecurity solution for individual AI products.

Th is is in line with established practice in cybersecurity, where risk assessments already play an important role,

particularly in the most widely used information security standards of the ISO 27000 series (ISO/IEC JTC 1/SC

27 2022). Crucia lly, within the scope of the AI Act , two levels of risk assessment should be considered:

●

The higher regulatory level risk assessment involving all other requirements as described in

Art icle 9.

●

Acybersecurity risk assessment to determine security measures appropriate to the specific risks

of the AI system and its components, whether AI or not, as described in Recita l 51 of the AI Act

and Annex II (2 .8) of the standardisation request.

9



<a name="br13"></a> 

Th is implies that, although the use of an AI system in a given specific context may be considered as high risk

from a regulatory standpoint (Anne x III of the AI Act ), the system could present limited cybersecurity risks due

to the way it is designed and operates. In the regulatory risk-assessment stage, the interplay with other

requirements of the AI Act should be considered. Further, the cybersecurity risk assessment will determine the

type and implementation method of the appropriate specific security risk mitigation measures for the system

and its components, ta king into account the internal architecture of the system and its intended application

context. In practice, cybersecurity measures will be balanced in complexity with other requirements for specific

AI systems.

As an illustration, an AI system designed to only be run locally by trained practitioners where the inputs to the

AI model cannot be directly controlled by an adversary may not need a high level of robustness against

adversarial attacks.

Guiding principle 3: Securing AI systems requires an integrated and continuous

approach using proven pra ct ices and AI-s pecific controls.

Th e cybersecurity of AI systems should rely on a combination of existing controls for software systems and AI-

specific controls on individual models. Th is should be applied at different system levels throughout the lifecycle

of the system following a holistic approach based on the security-in-depth and security-by-design principles. In

general, when possible, AI systems should not be treated differently from other known complex software

architectures. For instance, securing AI systems could take as a model already well developed cybersecurity

approaches for other complex digital systems, such as for cloud or Internet of Things (IoT) systems (Google

2023).

Howe ve r, there is no one-size-fits-all solution, as securing individual AI systems will depend on the outcomes

of the risk assessment considering the internal design of the system and its intended application context. An

approach following known security principles should be adopted to ensure that AI systems achieve compliance

with the cybersecurity requirement of the AI Act during their lifecycle.

Cybersecurity risks of AI systems may be addressed with the

opriate to the relevant

, as stated in Annex II (2.8) of the standardisation request of the Europea n Commis sion.

These risks can be addressed through known technical and organisational measures, either at the level of

components or at any suitable system level.

AI-s pe cific vulnerabilities may be addressed at AI component level using specific measures, whenever the state

of the art provides suitable solutions. However,they can also be addressed at system level using complementary

non-AI specific technical and organisational measures, possibly adapted to be used as measures to secure AI

components, if needed. Explicitly, it may even be more suitable or appropriate to the relevant circumstances

and estimated risks to handle an AI-s pe cific vulnerability at a higher system level following a security-in-depth

approach. Typica l AI-s pe cific cybersecurity challenges for machine learning models are listed in Sec. [2.2.](#br9)

Exa mple s of AI-s pe cific security controls at model level are adversarial training against specific types of evasion

attacks and knowledge distillation. At system level, examples of non- AI-s pe cific controls are access control

measures to restrict user interaction with the input to AI models, data sanitisation methods on inputs data, and

the broader set of security controls implementing the security in-depth and security by default paradigms.

It is important to note that, as it is the case with any software component, vulnerabilities of AI models need to

be assessed in the context role that the model plays within the internal architecture and design of the system,

and its interactions with other components.

Guiding principle 4: There are limit s in the state of the art for securing AI models.

A wide variety of AI technologies of different degrees of maturity coexis t in the current AI landscape, ranging

from traditional machine learning models to the latest large scale deep learning architectures (see Section 2 .1).

Ope n technological questions and challenges, including those for securing AI systems, are connected especially

to the more complex and newer models. Th is will likely lead to an increasing trend of complexity for securing

AI systems with the growing more widespread adoption of such advanced AI models.

10



<a name="br14"></a> 

Therefore, not all AI technologies might be ready for use in AI systems designed to be deployed in high-risk

scenarios, unless their limitations in terms of cybersecurity are properly addressed. Some examples for current

technological challenges in securing machine learning models are listed in Sec. 2.2.

As defined in the Annex II of the standardisation request, the harmonised standards that will be developed for

the AI Act are not expected to go beyond the a va ila ble state of the art. Th is should include AI-s pe cific security

measures that have reached a certain level of maturity in practice, but consequently, standards will not

specifically cover all limitations in AI technologies, particularly the emergent ones.

Instead, cybersecurity standards are expected to endorse elements of the presented integrated approach and

security-in-depth system perspective need not be limited themselves by any technological limitation in securing

individual AI models. Deploying AI-s pe cific security measures beyond the state of the start, i.e . not covered in

harmonised standards, remains possible, but it will be up to the provider of the AI system to ensure conformity,

as the presumption of compliance does not apply outside of coverage of harmonised standards.

11



<a name="br15"></a> 

4

Conclus ions

Th e global AI landscape is undertaking a rapid transformation, with new emergent technologies moving quickly

from the academic field into practical applications. Th is enables new use-cases that were considered until

recently out of reach using the a va ila ble technology. Whils t AI is expected to bring many benefits to the

Europea n society, it also creates new threats that need to be properly addressed.

In this context, the AI Act is of particular relevance, becoming a crucial element to ensure that AI systems

deployed in high-risk scenarios are safe to use and respect fundamental rights. Th is report focuses on the

cybersecurity requirement for high-risk AI systems, as set out in Art icle 15 of the regulation. Th e result of the

high level analysis carried out on the implementation of this requirement are the following four guiding

principles summarised hereafter:

1\. The focus of the AI Ac t is on AI systems. The structure of AI systems involves a range of internal

components, some of which are AI-rela ted, whilst others are not. Although AI models are essential

components of AI systems, they do not constitute AI systems on their own. The cybersecurity

requirement set out by the AI Act apply to the AI system as a whole and not directly to its internal

components.

2\. Complia nce wit h the AI Act necessarily requires a security risk assessment. In order to

ensure that an AI system complies with the cybersecurity requirement of the AI Act , a security risk

assessment should be conducted considering the internal architecture of the AI system and the

intended application context. Th is cybersecurity risk assessment, carried out in the context of the Ris k

Management System described in the Art icle 9 of the AI Act , a ims to identify the specific security

risks, translate the higher level cybersecurity requirement of the regulation down to specific

requirements for the components of the system, and implement the necessary mitigation measures.

3\. Securing AI systems requires an integrated and continuous approach using proven

practices and AI-s pecif ic controls. Th is process should leverage current cybersecurity practices

and procedures, using a combination of existing controls for software systems and AI-model specific

measures. AI systems are the sum of all their components and of their interactions. Aholistic

approach following the security-in-depth and security-by-design principles should be adopted to

ensure that AI systems achieve compliance with the cybersecurity requirement of the AI Act during

their lifecycle.

4\. There are limits in the state of the art for securing AI models. A wide variety of AI

technologies of different degrees of maturity coexist in the current AI landscape. Not all AI

technologies might be ready for use in AI systems designed to be deployed in high-risk scenarios,

unless their limitations in terms of cybersecurity are properly addressed. In some cases, particularly

for emergent AI technologies, there are inherent limitations that cannot be exclusively addressed at

the level of the AI model. In those cases, compliance with the cybersecurity requirement of the AI Ac t

can only be achieved following the holistic approach described earlier.

These guiding principles are intended to help all relevant stakeholders in addressing the cybersecurity

requirement for high-risk AI systems, as set out in Art icle 15 of the proposal of the Europea n Commission for

the AI Act .

In the context of the rapidly evolving AI landscape, harmonised standards developed for the AI Ac t are not

expected to cover approaches beyond the currently a va ila ble state of the art in AI cybersecurity. Howe ve r, these

limitations in the state of the art, do not necessarily impede the compliance of AI systems that ma ke use of

emergent AI technologies with the cybersecurity requirement of the AI Act , nor should they hinder the

development of standards. High-ris k AI systems can still achieve compliance if they mitigate appropriately the

overall cybersecurity risks of the system through other complementary measures, following an integrated

approach combining well-established cybersecurity practices and procedures with AI specific measures.

It is nonetheless important to acknowledge that this may not a lwa ys be possible and that for some high-risk AI

systems making use of emerging AI technologies it may not be feasible to achieve compliance with the

cybersecurity requirement of the AI Act using currently existing and mature cybersecurity techniques and

measures, highlighting the need for technological advancements in parallel to standardisation in this area.

12



<a name="br16"></a> 

References

Berghoff, Christia n, Battista Biggio, Elis a Brummel, Va s ilios Da nos, Thoma s Doms, He iko Ehrich, Ba rba ra

Hammer, et al.

\-

Whitepa per. Bundesa mt für Sicherheit in der Informationstechnik, Deutschland.

Bis hop, Christopher M. 2007. Pattern Re cognit ion and Ma chine Lea rning (Information Science and Statistics). 1st

ed. Springer.

Bomma sa ni, Ris hi, Dre w A. Hudson, Ehsan Ade li, Russ Altma n, Simran Arora , Sydney von Ar x, Micha el S.

http://arxiv.org/abs/2108.07258.

Cha pple, Mike , James Micha el Stewart, and Da rril Gibs on. 2021. (ISC)<sup>2</sup> CISSP Certified Information Systems

Security Professional Official Study Guide. 9th ed. Indianapolis: John Wile y and Sons.

Proposal for a Regula tion La ying down

-lex.europa.eu/legal-

content/EN/TXT/?uri=celex%3 A52 021SC0 084 .

cia l Intelligence (COM(2 021 )

-lex.e uropa .eu/lega l-content/EN/TXT/?uri=CELEX:5 2 02 1 PC0 20 6 .

Digita l

EU

Single

Ma rket

(COM(2 0 2

-lex.europa.eu/legal-

\-

content/EN/TXT/?uri=CELEX%3 A5 2 0 2 2 DC0 0 3 1 .

Elements and Amending Regula tion (EU) 2019/1020 (COM(2 022 ) 454

lex.europa .eu/lega l-content/EN/TXT/?uri=CELEX:5 2 02 2 PC0 4 54 .

Standardisation and the Europea n Committee for Electrotechnical Standardisation in Support of Union

\-

register/deta il?ref=C(2 023 )32 15.

Europea n

-lex.europa .eu/lega l-content/EN/TXT/?uri=CELEX:32 0 12 R1 02 5 .

Goodfellow, Ian J., Yoshua Be ngio, and Aa ron Courville. 2016. Deep Lea rning. Ca mbridge, MA, US A: MIT Press.

Google Safety & Security (blog). 2023.

https://blog.google/technology/safety-security/introducing-googles-secure-ai-framework/.

SO/IEC 27001 - Information Security Management Systems -

https://www.iso.org/standard/27001.

ENISA. https://doi.org/10.2824/874249.

Nai Fovino, Igor, Ge ra ldine Ba rry, Stephane Cha udron, Iwen Cois e l, Ma rion Dewa r, He nrik Junklewitz, G.

\- Joint

Resea rch Centre. https://doi.org/10.2760/352218.

OEC

\-

ilibrary.org/content/paper/f94df8ec-en.

Papernot, Nicola s , Patrick McDa nie l, Arun

19\.

-30 Rev 1. NIST. ht t ps ://doi.org/NIST.SP.8 0 0 -

30r1.

Shostack, Adam. 2014. Threa t Modeling: Designing for Security. 1st ed. Wile y Publishing.

13



<a name="br17"></a> 

Soler Ga rrido, Josep, De lia Fa no Yela, Ce cilia Panigutti, He nrik Junklewitz, Rona n Ha mon, Tatjana Eva s, Antoine -

rdisation Work Pla n

-NA-31-518-EN-N (online). https://doi.org/10.2760/5847 (online).

Tabassi, Elha m, Ke vin J. Burns , Micha el Ha djimicha el, Andres D. Molina -

Ta xonomy and Terminology of

https://doi.org/1 0.6 028 /NIST.IR.826 9 -dra ft .

14



<a name="br18"></a> 

Lis t of a bbrevia t ions

AI

Artificia l Intelligence

CEN

CENELEC

CRA

ETSI

ISO

Europea n Committee for Standardization

Europea n Committee for Electrotechnical Standardization

Cybe r Re s ilie nce Act

Europea n Telecommunications Standards Institute

International Organization for Standardization

Internet of Things

IoT

OECD

Organisation for Economic Co-opera tion and Development

15



<a name="br19"></a> 

GETTING IN TOUCH WITH THE EU

In person

All over the European Union there are hundreds of Europe Direct centres. You can find the address of the centre nearest you online

[(](https://european-union.europa.eu/contact-eu/meet-us_en)[european-union.europa.eu/contact-eu/meet-us_en](https://european-union.europa.eu/contact-eu/meet-us_en)[).](https://european-union.europa.eu/contact-eu/meet-us_en)

On the phone or in writing

Europe Direct is a service that answers your questions about the European Union. You can contact this service:

by freephone: 00 800 6 7 8 9 10 11 (certain operators may charge for these calls),

at the following standard number: +32 22999696,

via the following form[:](https://european-union.europa.eu/contact-eu/write-us_en)[ ](https://european-union.europa.eu/contact-eu/write-us_en)[european-union.europa.eu/contact-eu/write-us_en](https://european-union.europa.eu/contact-eu/write-us_en)[.](https://european-union.europa.eu/contact-eu/write-us_en)

FINDING INFORMATION ABOUT THE EU

Online

Information about the European Union in all the official languages of the EU is available on the Europa website [(](https://european-union.europa.eu/index_en)[european-](https://european-union.europa.eu/index_en)

[union.europa.eu](https://european-union.europa.eu/index_en)[).](https://european-union.europa.eu/index_en)

EU publications

You can view or order EU publications at [op.europa.eu/en/publications](https://op.europa.eu/en/publications)[.](https://op.europa.eu/en/publications)[ ](https://op.europa.eu/en/publications)Multiple copies of free publications can be obtained by

contacting Europe Direct or your local documentation centre [(](https://european-union.europa.eu/contact-eu/meet-us_en)[european-union.europa.eu/contact-eu/meet-us_en](https://european-union.europa.eu/contact-eu/meet-us_en)[).](https://european-union.europa.eu/contact-eu/meet-us_en)

EU law and related documents

For access to legal information from the EU, including all EU law since 1951 in all the official language versions, go to EUR- Le x [(](https://eur-lex.europa.eu/)[eur-](https://eur-lex.europa.eu/)

[lex.europa.eu](https://eur-lex.europa.eu/)[).](https://eur-lex.europa.eu/)

Open data from the EU

The porta[l](https://data.europa.eu/en)[ ](https://data.europa.eu/en)[data.europa.eu](https://data.europa.eu/en)[ ](https://data.europa.eu/en)provides access to open datasets from the EUinstitutions, bodies and agencies. These can be downloaded

and reused for free, for both commercial and non-commercial purposes. The portal also provides access to a wealth of datasets

from European countries.



<a name="br20"></a> 

