QT += network

HEADERS += \
# Models
    $${PWD}/OAIApiResponse_List_PublishedEarlyDayMotion_.h \
    $${PWD}/OAIApiResponse_List_PublishedOralQuestionTime_.h \
    $${PWD}/OAIApiResponse_List_PublishedOralQuestion_.h \
    $${PWD}/OAIApiResponse_List_PublishedWrittenQuestion_.h \
    $${PWD}/OAIApiResponse_Object_.h \
    $${PWD}/OAIApiResponse_PublishedEarlyDayMotionDetails_.h \
    $${PWD}/OAIMemberForDate.h \
    $${PWD}/OAIPagingInfo.h \
    $${PWD}/OAIPublishedEarlyDayMotion.h \
    $${PWD}/OAIPublishedEarlyDayMotionDetails.h \
    $${PWD}/OAIPublishedEarlyDayMotionQueryParameters.h \
    $${PWD}/OAIPublishedEarlyDayMotionSponsor.h \
    $${PWD}/OAIPublishedOralQuestion.h \
    $${PWD}/OAIPublishedOralQuestionQueryParameters.h \
    $${PWD}/OAIPublishedOralQuestionTime.h \
    $${PWD}/OAIPublishedOralQuestionTimeQueryParameters.h \
    $${PWD}/OAIPublishedWrittenQuestion.h \
    $${PWD}/OAIStatusCount.h \
# APIs
    $${PWD}/OAIEarlyDayMotionsApi.h \
    $${PWD}/OAIOralQuestionTimesApi.h \
    $${PWD}/OAIOralQuestionsApi.h \
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
    $${PWD}/OAIApiResponse_List_PublishedEarlyDayMotion_.cpp \
    $${PWD}/OAIApiResponse_List_PublishedOralQuestionTime_.cpp \
    $${PWD}/OAIApiResponse_List_PublishedOralQuestion_.cpp \
    $${PWD}/OAIApiResponse_List_PublishedWrittenQuestion_.cpp \
    $${PWD}/OAIApiResponse_Object_.cpp \
    $${PWD}/OAIApiResponse_PublishedEarlyDayMotionDetails_.cpp \
    $${PWD}/OAIMemberForDate.cpp \
    $${PWD}/OAIPagingInfo.cpp \
    $${PWD}/OAIPublishedEarlyDayMotion.cpp \
    $${PWD}/OAIPublishedEarlyDayMotionDetails.cpp \
    $${PWD}/OAIPublishedEarlyDayMotionQueryParameters.cpp \
    $${PWD}/OAIPublishedEarlyDayMotionSponsor.cpp \
    $${PWD}/OAIPublishedOralQuestion.cpp \
    $${PWD}/OAIPublishedOralQuestionQueryParameters.cpp \
    $${PWD}/OAIPublishedOralQuestionTime.cpp \
    $${PWD}/OAIPublishedOralQuestionTimeQueryParameters.cpp \
    $${PWD}/OAIPublishedWrittenQuestion.cpp \
    $${PWD}/OAIStatusCount.cpp \
# APIs
    $${PWD}/OAIEarlyDayMotionsApi.cpp \
    $${PWD}/OAIOralQuestionTimesApi.cpp \
    $${PWD}/OAIOralQuestionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
