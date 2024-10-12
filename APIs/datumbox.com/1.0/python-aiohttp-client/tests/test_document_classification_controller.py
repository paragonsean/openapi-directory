# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_adult_content_detection(client):
    """Test case for adult_content_detection

    Classifies the Document as adult or noadult
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/AdultContentDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_commercial_detection(client):
    """Test case for commercial_detection

    Classifies the Document as commercial or nocommercial
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/CommercialDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_educational_detection(client):
    """Test case for educational_detection

    Classifies the Document as educational or noeducational
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/EducationalDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_gender_detection(client):
    """Test case for gender_detection

    Gender Detection Service
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/GenderDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_language_detection(client):
    """Test case for language_detection

    Identifies the Language of the Document
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/LanguageDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_readability_assessment(client):
    """Test case for readability_assessment

    Evaluates the Readability of the Document
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/ReadabilityAssessment.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_sentiment_analysis(client):
    """Test case for sentiment_analysis

    Identifies the Sentiment of the Document
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/SentimentAnalysis.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_spam_detection(client):
    """Test case for spam_detection

    Classifies the Document as spam or nospam
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/SpamDetection.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_subjectivity_analysis(client):
    """Test case for subjectivity_analysis

    Classifies Document as Subjective or Objective
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/SubjectivityAnalysis.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_topic_classification(client):
    """Test case for topic_classification

    Identifies the Topic of the Document
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/TopicClassification.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_twitter_sentiment_analysis(client):
    """Test case for twitter_sentiment_analysis

    Identifies the Sentiment of Twitter Messages
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'api_key': 'api_key_example',
        'text': 'text_example'
        }
    response = await client.request(
        method='POST',
        path='/1.0/TwitterSentimentAnalysis.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

