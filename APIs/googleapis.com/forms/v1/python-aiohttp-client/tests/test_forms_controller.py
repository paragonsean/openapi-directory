# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_update_form_request import BatchUpdateFormRequest
from openapi_server.models.batch_update_form_response import BatchUpdateFormResponse
from openapi_server.models.create_watch_request import CreateWatchRequest
from openapi_server.models.form import Form
from openapi_server.models.form_response import FormResponse
from openapi_server.models.list_form_responses_response import ListFormResponsesResponse
from openapi_server.models.list_watches_response import ListWatchesResponse
from openapi_server.models.watch import Watch


pytestmark = pytest.mark.asyncio

async def test_forms_forms_batch_update(client):
    """Test case for forms_forms_batch_update

    
    """
    body = {"requests":[{"moveItem":{"originalLocation":{"index":0},"newLocation":{"index":0}},"deleteItem":{"location":{"index":0}},"createItem":{"item":{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"},"location":{"index":0}},"updateItem":{"item":{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"},"location":{"index":0},"updateMask":"updateMask"},"updateSettings":{"settings":{"quizSettings":{"isQuiz":True}},"updateMask":"updateMask"},"updateFormInfo":{"updateMask":"updateMask","info":{"description":"description","documentTitle":"documentTitle","title":"title"}}},{"moveItem":{"originalLocation":{"index":0},"newLocation":{"index":0}},"deleteItem":{"location":{"index":0}},"createItem":{"item":{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"},"location":{"index":0}},"updateItem":{"item":{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"},"location":{"index":0},"updateMask":"updateMask"},"updateSettings":{"settings":{"quizSettings":{"isQuiz":True}},"updateMask":"updateMask"},"updateFormInfo":{"updateMask":"updateMask","info":{"description":"description","documentTitle":"documentTitle","title":"title"}}}],"includeFormInResponse":True,"writeControl":{"targetRevisionId":"targetRevisionId","requiredRevisionId":"requiredRevisionId"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/forms/{form_idbatch_updat}'.format(form_id='form_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_create(client):
    """Test case for forms_forms_create

    
    """
    body = {"formId":"formId","revisionId":"revisionId","settings":{"quizSettings":{"isQuiz":True}},"responderUri":"responderUri","items":[{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"},{"videoItem":{"caption":"caption","video":{"youtubeUri":"youtubeUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"itemId":"itemId","questionItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"question":{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}},"questionGroupItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"grid":{"columns":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"shuffleQuestions":True},"questions":[{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}},{"choiceQuestion":{"options":[{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"},{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}},"goToSectionId":"goToSectionId","goToAction":"GO_TO_ACTION_UNSPECIFIED","isOther":True,"value":"value"}],"shuffle":True,"type":"CHOICE_TYPE_UNSPECIFIED"},"questionId":"questionId","dateQuestion":{"includeTime":True,"includeYear":True},"grading":{"whenWrong":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"pointValue":1,"generalFeedback":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"whenRight":{"material":[{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}},{"link":{"displayText":"displayText","uri":"uri"},"video":{"displayText":"displayText","youtubeUri":"youtubeUri"}}],"text":"text"},"correctAnswers":{"answers":[{"value":"value"},{"value":"value"}]}},"textQuestion":{"paragraph":True},"fileUploadQuestion":{"types":["FILE_TYPE_UNSPECIFIED","FILE_TYPE_UNSPECIFIED"],"maxFileSize":"maxFileSize","folderId":"folderId","maxFiles":6},"rowQuestion":{"title":"title"},"required":True,"scaleQuestion":{"high":5,"low":5,"highLabel":"highLabel","lowLabel":"lowLabel"},"timeQuestion":{"duration":True}}]},"textItem":"{}","description":"description","title":"title","imageItem":{"image":{"altText":"altText","sourceUri":"sourceUri","contentUri":"contentUri","properties":{"width":0,"alignment":"ALIGNMENT_UNSPECIFIED"}}},"pageBreakItem":"{}"}],"linkedSheetId":"linkedSheetId","info":{"description":"description","documentTitle":"documentTitle","title":"title"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/forms',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_get(client):
    """Test case for forms_forms_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/forms/{form_id}'.format(form_id='form_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_responses_get(client):
    """Test case for forms_forms_responses_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/forms/{form_id}/responses/{response_id}'.format(form_id='form_id_example', response_id='response_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_responses_list(client):
    """Test case for forms_forms_responses_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/forms/{form_id}/responses'.format(form_id='form_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_watches_create(client):
    """Test case for forms_forms_watches_create

    
    """
    body = {"watch":{"expireTime":"expireTime","createTime":"createTime","errorType":"ERROR_TYPE_UNSPECIFIED","eventType":"EVENT_TYPE_UNSPECIFIED","id":"id","state":"STATE_UNSPECIFIED","target":{"topic":{"topicName":"topicName"}}},"watchId":"watchId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/forms/{form_id}/watches'.format(form_id='form_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_watches_delete(client):
    """Test case for forms_forms_watches_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/forms/{form_id}/watches/{watch_id}'.format(form_id='form_id_example', watch_id='watch_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_watches_list(client):
    """Test case for forms_forms_watches_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/forms/{form_id}/watches'.format(form_id='form_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forms_forms_watches_renew(client):
    """Test case for forms_forms_watches_renew

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/forms/{form_id}/watches/{watch_idrene}'.format(form_id='form_id_example', watch_id='watch_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

