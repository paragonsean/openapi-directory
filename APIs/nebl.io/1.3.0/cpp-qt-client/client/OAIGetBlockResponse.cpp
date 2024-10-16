/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetBlockResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetBlockResponse::OAIGetBlockResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetBlockResponse::OAIGetBlockResponse() {
    this->initializeModel();
}

OAIGetBlockResponse::~OAIGetBlockResponse() {}

void OAIGetBlockResponse::initializeModel() {

    m_bits_isSet = false;
    m_bits_isValid = false;

    m_confirmations_isSet = false;
    m_confirmations_isValid = false;

    m_difficulty_isSet = false;
    m_difficulty_isValid = false;

    m_hash_isSet = false;
    m_hash_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_merkleroot_isSet = false;
    m_merkleroot_isValid = false;

    m_nextblockhash_isSet = false;
    m_nextblockhash_isValid = false;

    m_nonce_isSet = false;
    m_nonce_isValid = false;

    m_previousblockhash_isSet = false;
    m_previousblockhash_isValid = false;

    m_reward_isSet = false;
    m_reward_isValid = false;

    m_size_isSet = false;
    m_size_isValid = false;

    m_time_isSet = false;
    m_time_isValid = false;

    m_tx_isSet = false;
    m_tx_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIGetBlockResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetBlockResponse::fromJsonObject(QJsonObject json) {

    m_bits_isValid = ::OpenAPI::fromJsonValue(m_bits, json[QString("bits")]);
    m_bits_isSet = !json[QString("bits")].isNull() && m_bits_isValid;

    m_confirmations_isValid = ::OpenAPI::fromJsonValue(m_confirmations, json[QString("confirmations")]);
    m_confirmations_isSet = !json[QString("confirmations")].isNull() && m_confirmations_isValid;

    m_difficulty_isValid = ::OpenAPI::fromJsonValue(m_difficulty, json[QString("difficulty")]);
    m_difficulty_isSet = !json[QString("difficulty")].isNull() && m_difficulty_isValid;

    m_hash_isValid = ::OpenAPI::fromJsonValue(m_hash, json[QString("hash")]);
    m_hash_isSet = !json[QString("hash")].isNull() && m_hash_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_merkleroot_isValid = ::OpenAPI::fromJsonValue(m_merkleroot, json[QString("merkleroot")]);
    m_merkleroot_isSet = !json[QString("merkleroot")].isNull() && m_merkleroot_isValid;

    m_nextblockhash_isValid = ::OpenAPI::fromJsonValue(m_nextblockhash, json[QString("nextblockhash")]);
    m_nextblockhash_isSet = !json[QString("nextblockhash")].isNull() && m_nextblockhash_isValid;

    m_nonce_isValid = ::OpenAPI::fromJsonValue(m_nonce, json[QString("nonce")]);
    m_nonce_isSet = !json[QString("nonce")].isNull() && m_nonce_isValid;

    m_previousblockhash_isValid = ::OpenAPI::fromJsonValue(m_previousblockhash, json[QString("previousblockhash")]);
    m_previousblockhash_isSet = !json[QString("previousblockhash")].isNull() && m_previousblockhash_isValid;

    m_reward_isValid = ::OpenAPI::fromJsonValue(m_reward, json[QString("reward")]);
    m_reward_isSet = !json[QString("reward")].isNull() && m_reward_isValid;

    m_size_isValid = ::OpenAPI::fromJsonValue(m_size, json[QString("size")]);
    m_size_isSet = !json[QString("size")].isNull() && m_size_isValid;

    m_time_isValid = ::OpenAPI::fromJsonValue(m_time, json[QString("time")]);
    m_time_isSet = !json[QString("time")].isNull() && m_time_isValid;

    m_tx_isValid = ::OpenAPI::fromJsonValue(m_tx, json[QString("tx")]);
    m_tx_isSet = !json[QString("tx")].isNull() && m_tx_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIGetBlockResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetBlockResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_bits_isSet) {
        obj.insert(QString("bits"), ::OpenAPI::toJsonValue(m_bits));
    }
    if (m_confirmations_isSet) {
        obj.insert(QString("confirmations"), ::OpenAPI::toJsonValue(m_confirmations));
    }
    if (m_difficulty_isSet) {
        obj.insert(QString("difficulty"), ::OpenAPI::toJsonValue(m_difficulty));
    }
    if (m_hash_isSet) {
        obj.insert(QString("hash"), ::OpenAPI::toJsonValue(m_hash));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_merkleroot_isSet) {
        obj.insert(QString("merkleroot"), ::OpenAPI::toJsonValue(m_merkleroot));
    }
    if (m_nextblockhash_isSet) {
        obj.insert(QString("nextblockhash"), ::OpenAPI::toJsonValue(m_nextblockhash));
    }
    if (m_nonce_isSet) {
        obj.insert(QString("nonce"), ::OpenAPI::toJsonValue(m_nonce));
    }
    if (m_previousblockhash_isSet) {
        obj.insert(QString("previousblockhash"), ::OpenAPI::toJsonValue(m_previousblockhash));
    }
    if (m_reward_isSet) {
        obj.insert(QString("reward"), ::OpenAPI::toJsonValue(m_reward));
    }
    if (m_size_isSet) {
        obj.insert(QString("size"), ::OpenAPI::toJsonValue(m_size));
    }
    if (m_time_isSet) {
        obj.insert(QString("time"), ::OpenAPI::toJsonValue(m_time));
    }
    if (m_tx.size() > 0) {
        obj.insert(QString("tx"), ::OpenAPI::toJsonValue(m_tx));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIGetBlockResponse::getBits() const {
    return m_bits;
}
void OAIGetBlockResponse::setBits(const QString &bits) {
    m_bits = bits;
    m_bits_isSet = true;
}

bool OAIGetBlockResponse::is_bits_Set() const{
    return m_bits_isSet;
}

bool OAIGetBlockResponse::is_bits_Valid() const{
    return m_bits_isValid;
}

double OAIGetBlockResponse::getConfirmations() const {
    return m_confirmations;
}
void OAIGetBlockResponse::setConfirmations(const double &confirmations) {
    m_confirmations = confirmations;
    m_confirmations_isSet = true;
}

bool OAIGetBlockResponse::is_confirmations_Set() const{
    return m_confirmations_isSet;
}

bool OAIGetBlockResponse::is_confirmations_Valid() const{
    return m_confirmations_isValid;
}

double OAIGetBlockResponse::getDifficulty() const {
    return m_difficulty;
}
void OAIGetBlockResponse::setDifficulty(const double &difficulty) {
    m_difficulty = difficulty;
    m_difficulty_isSet = true;
}

bool OAIGetBlockResponse::is_difficulty_Set() const{
    return m_difficulty_isSet;
}

bool OAIGetBlockResponse::is_difficulty_Valid() const{
    return m_difficulty_isValid;
}

QString OAIGetBlockResponse::getHash() const {
    return m_hash;
}
void OAIGetBlockResponse::setHash(const QString &hash) {
    m_hash = hash;
    m_hash_isSet = true;
}

bool OAIGetBlockResponse::is_hash_Set() const{
    return m_hash_isSet;
}

bool OAIGetBlockResponse::is_hash_Valid() const{
    return m_hash_isValid;
}

double OAIGetBlockResponse::getHeight() const {
    return m_height;
}
void OAIGetBlockResponse::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAIGetBlockResponse::is_height_Set() const{
    return m_height_isSet;
}

bool OAIGetBlockResponse::is_height_Valid() const{
    return m_height_isValid;
}

QString OAIGetBlockResponse::getMerkleroot() const {
    return m_merkleroot;
}
void OAIGetBlockResponse::setMerkleroot(const QString &merkleroot) {
    m_merkleroot = merkleroot;
    m_merkleroot_isSet = true;
}

bool OAIGetBlockResponse::is_merkleroot_Set() const{
    return m_merkleroot_isSet;
}

bool OAIGetBlockResponse::is_merkleroot_Valid() const{
    return m_merkleroot_isValid;
}

QString OAIGetBlockResponse::getNextblockhash() const {
    return m_nextblockhash;
}
void OAIGetBlockResponse::setNextblockhash(const QString &nextblockhash) {
    m_nextblockhash = nextblockhash;
    m_nextblockhash_isSet = true;
}

bool OAIGetBlockResponse::is_nextblockhash_Set() const{
    return m_nextblockhash_isSet;
}

bool OAIGetBlockResponse::is_nextblockhash_Valid() const{
    return m_nextblockhash_isValid;
}

double OAIGetBlockResponse::getNonce() const {
    return m_nonce;
}
void OAIGetBlockResponse::setNonce(const double &nonce) {
    m_nonce = nonce;
    m_nonce_isSet = true;
}

bool OAIGetBlockResponse::is_nonce_Set() const{
    return m_nonce_isSet;
}

bool OAIGetBlockResponse::is_nonce_Valid() const{
    return m_nonce_isValid;
}

QString OAIGetBlockResponse::getPreviousblockhash() const {
    return m_previousblockhash;
}
void OAIGetBlockResponse::setPreviousblockhash(const QString &previousblockhash) {
    m_previousblockhash = previousblockhash;
    m_previousblockhash_isSet = true;
}

bool OAIGetBlockResponse::is_previousblockhash_Set() const{
    return m_previousblockhash_isSet;
}

bool OAIGetBlockResponse::is_previousblockhash_Valid() const{
    return m_previousblockhash_isValid;
}

double OAIGetBlockResponse::getReward() const {
    return m_reward;
}
void OAIGetBlockResponse::setReward(const double &reward) {
    m_reward = reward;
    m_reward_isSet = true;
}

bool OAIGetBlockResponse::is_reward_Set() const{
    return m_reward_isSet;
}

bool OAIGetBlockResponse::is_reward_Valid() const{
    return m_reward_isValid;
}

double OAIGetBlockResponse::getSize() const {
    return m_size;
}
void OAIGetBlockResponse::setSize(const double &size) {
    m_size = size;
    m_size_isSet = true;
}

bool OAIGetBlockResponse::is_size_Set() const{
    return m_size_isSet;
}

bool OAIGetBlockResponse::is_size_Valid() const{
    return m_size_isValid;
}

double OAIGetBlockResponse::getTime() const {
    return m_time;
}
void OAIGetBlockResponse::setTime(const double &time) {
    m_time = time;
    m_time_isSet = true;
}

bool OAIGetBlockResponse::is_time_Set() const{
    return m_time_isSet;
}

bool OAIGetBlockResponse::is_time_Valid() const{
    return m_time_isValid;
}

QList<QString> OAIGetBlockResponse::getTx() const {
    return m_tx;
}
void OAIGetBlockResponse::setTx(const QList<QString> &tx) {
    m_tx = tx;
    m_tx_isSet = true;
}

bool OAIGetBlockResponse::is_tx_Set() const{
    return m_tx_isSet;
}

bool OAIGetBlockResponse::is_tx_Valid() const{
    return m_tx_isValid;
}

double OAIGetBlockResponse::getVersion() const {
    return m_version;
}
void OAIGetBlockResponse::setVersion(const double &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIGetBlockResponse::is_version_Set() const{
    return m_version_isSet;
}

bool OAIGetBlockResponse::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIGetBlockResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_bits_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_confirmations_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_difficulty_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_hash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merkleroot_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nextblockhash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nonce_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_previousblockhash_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_size_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tx.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetBlockResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
