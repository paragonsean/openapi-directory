QT += network

HEADERS += \
# Models
    $${PWD}/OAIChangelog.h \
    $${PWD}/OAICustomPage.h \
    $${PWD}/OAIDoc.h \
    $${PWD}/OAIVersion.h \
# APIs
    $${PWD}/OAIAPISpecificationApi.h \
    $${PWD}/OAICategoriesApi.h \
    $${PWD}/OAIChangelogApi.h \
    $${PWD}/OAICustomPagesApi.h \
    $${PWD}/OAIDocsApi.h \
    $${PWD}/OAIErrorsApi.h \
    $${PWD}/OAIProjectsApi.h \
    $${PWD}/OAISwaggerApi.h \
    $${PWD}/OAIVersionApi.h \
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
    $${PWD}/OAIChangelog.cpp \
    $${PWD}/OAICustomPage.cpp \
    $${PWD}/OAIDoc.cpp \
    $${PWD}/OAIVersion.cpp \
# APIs
    $${PWD}/OAIAPISpecificationApi.cpp \
    $${PWD}/OAICategoriesApi.cpp \
    $${PWD}/OAIChangelogApi.cpp \
    $${PWD}/OAICustomPagesApi.cpp \
    $${PWD}/OAIDocsApi.cpp \
    $${PWD}/OAIErrorsApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
    $${PWD}/OAISwaggerApi.cpp \
    $${PWD}/OAIVersionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
