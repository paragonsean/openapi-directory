QT += network

HEADERS += \
# Models
    $${PWD}/OAIContentHash.h \
    $${PWD}/OAIContentLink.h \
    $${PWD}/OAIJobStream.h \
    $${PWD}/OAIJobStreamListResult.h \
    $${PWD}/OAIJobStreamProperties.h \
    $${PWD}/OAIRunbook.h \
    $${PWD}/OAIRunbookCreateOrUpdateDraftParameters.h \
    $${PWD}/OAIRunbookCreateOrUpdateDraftProperties.h \
    $${PWD}/OAIRunbookCreateOrUpdateParameters.h \
    $${PWD}/OAIRunbookCreateOrUpdateProperties.h \
    $${PWD}/OAIRunbookDraft.h \
    $${PWD}/OAIRunbookDraftUndoEditResult.h \
    $${PWD}/OAIRunbookListResult.h \
    $${PWD}/OAIRunbookParameter.h \
    $${PWD}/OAIRunbookProperties.h \
    $${PWD}/OAIRunbookUpdateParameters.h \
    $${PWD}/OAIRunbookUpdateProperties.h \
    $${PWD}/OAIRunbook_ListByAutomationAccount_default_response.h \
    $${PWD}/OAITestJob.h \
    $${PWD}/OAITestJobCreateParameters.h \
# APIs
    $${PWD}/OAIRunbookApi.h \
    $${PWD}/OAIRunbookDraftApi.h \
    $${PWD}/OAITestJobApi.h \
    $${PWD}/OAITestJobStreamApi.h \
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
    $${PWD}/OAIContentHash.cpp \
    $${PWD}/OAIContentLink.cpp \
    $${PWD}/OAIJobStream.cpp \
    $${PWD}/OAIJobStreamListResult.cpp \
    $${PWD}/OAIJobStreamProperties.cpp \
    $${PWD}/OAIRunbook.cpp \
    $${PWD}/OAIRunbookCreateOrUpdateDraftParameters.cpp \
    $${PWD}/OAIRunbookCreateOrUpdateDraftProperties.cpp \
    $${PWD}/OAIRunbookCreateOrUpdateParameters.cpp \
    $${PWD}/OAIRunbookCreateOrUpdateProperties.cpp \
    $${PWD}/OAIRunbookDraft.cpp \
    $${PWD}/OAIRunbookDraftUndoEditResult.cpp \
    $${PWD}/OAIRunbookListResult.cpp \
    $${PWD}/OAIRunbookParameter.cpp \
    $${PWD}/OAIRunbookProperties.cpp \
    $${PWD}/OAIRunbookUpdateParameters.cpp \
    $${PWD}/OAIRunbookUpdateProperties.cpp \
    $${PWD}/OAIRunbook_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAITestJob.cpp \
    $${PWD}/OAITestJobCreateParameters.cpp \
# APIs
    $${PWD}/OAIRunbookApi.cpp \
    $${PWD}/OAIRunbookDraftApi.cpp \
    $${PWD}/OAITestJobApi.cpp \
    $${PWD}/OAITestJobStreamApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
