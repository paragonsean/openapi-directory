QT += network

HEADERS += \
# Models
    $${PWD}/OAIArticlesList.h \
    $${PWD}/OAIArticlesList_articles_inner.h \
    $${PWD}/OAIBlogList.h \
    $${PWD}/OAIBlogList_blog_inner_inner.h \
    $${PWD}/OAIBlogPage.h \
    $${PWD}/OAIGlossaryList.h \
    $${PWD}/OAIGlossaryList_glossary_inner.h \
    $${PWD}/OAIGlossaryPage.h \
    $${PWD}/OAIPage.h \
    $${PWD}/OAIQuestionPage.h \
    $${PWD}/OAIQuestionsList.h \
    $${PWD}/OAIQuestionsList_questions_inner.h \
    $${PWD}/OAIStatePage.h \
    $${PWD}/OAIStatesList.h \
    $${PWD}/OAIStatesList_states_inner_inner.h \
    $${PWD}/OAITopicsList.h \
    $${PWD}/OAITopicsList_topics_inner.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIArticlesList.cpp \
    $${PWD}/OAIArticlesList_articles_inner.cpp \
    $${PWD}/OAIBlogList.cpp \
    $${PWD}/OAIBlogList_blog_inner_inner.cpp \
    $${PWD}/OAIBlogPage.cpp \
    $${PWD}/OAIGlossaryList.cpp \
    $${PWD}/OAIGlossaryList_glossary_inner.cpp \
    $${PWD}/OAIGlossaryPage.cpp \
    $${PWD}/OAIPage.cpp \
    $${PWD}/OAIQuestionPage.cpp \
    $${PWD}/OAIQuestionsList.cpp \
    $${PWD}/OAIQuestionsList_questions_inner.cpp \
    $${PWD}/OAIStatePage.cpp \
    $${PWD}/OAIStatesList.cpp \
    $${PWD}/OAIStatesList_states_inner_inner.cpp \
    $${PWD}/OAITopicsList.cpp \
    $${PWD}/OAITopicsList_topics_inner.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
