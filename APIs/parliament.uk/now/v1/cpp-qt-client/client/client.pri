QT += network

HEADERS += \
# Models
    $${PWD}/OAIAnnunciatorMessageType.h \
    $${PWD}/OAIContentStyle.h \
    $${PWD}/OAIContentType.h \
    $${PWD}/OAIHorizontalAlignment.h \
    $${PWD}/OAIHouseMembershipViewModel.h \
    $${PWD}/OAILineViewModel.h \
    $${PWD}/OAIMemberViewModel.h \
    $${PWD}/OAIMessageViewModel.h \
    $${PWD}/OAIPartyViewModel.h \
    $${PWD}/OAIScrollingMessageAlertType.h \
    $${PWD}/OAIScrollingMessageViewModel.h \
    $${PWD}/OAISlideType.h \
    $${PWD}/OAISlideViewModel.h \
    $${PWD}/OAISounds.h \
    $${PWD}/OAIVerticalAlignment.h \
# APIs
    $${PWD}/OAIMessageApi.h \
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
    $${PWD}/OAIAnnunciatorMessageType.cpp \
    $${PWD}/OAIContentStyle.cpp \
    $${PWD}/OAIContentType.cpp \
    $${PWD}/OAIHorizontalAlignment.cpp \
    $${PWD}/OAIHouseMembershipViewModel.cpp \
    $${PWD}/OAILineViewModel.cpp \
    $${PWD}/OAIMemberViewModel.cpp \
    $${PWD}/OAIMessageViewModel.cpp \
    $${PWD}/OAIPartyViewModel.cpp \
    $${PWD}/OAIScrollingMessageAlertType.cpp \
    $${PWD}/OAIScrollingMessageViewModel.cpp \
    $${PWD}/OAISlideType.cpp \
    $${PWD}/OAISlideViewModel.cpp \
    $${PWD}/OAISounds.cpp \
    $${PWD}/OAIVerticalAlignment.cpp \
# APIs
    $${PWD}/OAIMessageApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
