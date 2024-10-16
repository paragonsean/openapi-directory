/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIGetBlockV2_200_response.h
 *
 * 
 */

#ifndef OAIGetBlockV2_200_response_H
#define OAIGetBlockV2_200_response_H

#include <QJsonObject>

#include "OAIGetBlockV2_200_response_txs_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetBlockV2_200_response_txs_inner;

class OAIGetBlockV2_200_response : public OAIObject {
public:
    OAIGetBlockV2_200_response();
    OAIGetBlockV2_200_response(QString json);
    ~OAIGetBlockV2_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBits() const;
    void setBits(const QString &bits);
    bool is_bits_Set() const;
    bool is_bits_Valid() const;

    qint32 getConfirmations() const;
    void setConfirmations(const qint32 &confirmations);
    bool is_confirmations_Set() const;
    bool is_confirmations_Valid() const;

    QString getDifficulty() const;
    void setDifficulty(const QString &difficulty);
    bool is_difficulty_Set() const;
    bool is_difficulty_Valid() const;

    QString getHash() const;
    void setHash(const QString &hash);
    bool is_hash_Set() const;
    bool is_hash_Valid() const;

    qint32 getHeight() const;
    void setHeight(const qint32 &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    qint32 getItemsOnPage() const;
    void setItemsOnPage(const qint32 &items_on_page);
    bool is_items_on_page_Set() const;
    bool is_items_on_page_Valid() const;

    QString getMerkleRoot() const;
    void setMerkleRoot(const QString &merkle_root);
    bool is_merkle_root_Set() const;
    bool is_merkle_root_Valid() const;

    QString getNextBlockHash() const;
    void setNextBlockHash(const QString &next_block_hash);
    bool is_next_block_hash_Set() const;
    bool is_next_block_hash_Valid() const;

    QString getNonce() const;
    void setNonce(const QString &nonce);
    bool is_nonce_Set() const;
    bool is_nonce_Valid() const;

    qint32 getPage() const;
    void setPage(const qint32 &page);
    bool is_page_Set() const;
    bool is_page_Valid() const;

    QString getPreviousBlockHash() const;
    void setPreviousBlockHash(const QString &previous_block_hash);
    bool is_previous_block_hash_Set() const;
    bool is_previous_block_hash_Valid() const;

    qint32 getSize() const;
    void setSize(const qint32 &size);
    bool is_size_Set() const;
    bool is_size_Valid() const;

    qint32 getTime() const;
    void setTime(const qint32 &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    qint32 getTotalPages() const;
    void setTotalPages(const qint32 &total_pages);
    bool is_total_pages_Set() const;
    bool is_total_pages_Valid() const;

    qint32 getTxCount() const;
    void setTxCount(const qint32 &tx_count);
    bool is_tx_count_Set() const;
    bool is_tx_count_Valid() const;

    QList<OAIGetBlockV2_200_response_txs_inner> getTxs() const;
    void setTxs(const QList<OAIGetBlockV2_200_response_txs_inner> &txs);
    bool is_txs_Set() const;
    bool is_txs_Valid() const;

    qint32 getVersion() const;
    void setVersion(const qint32 &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_bits;
    bool m_bits_isSet;
    bool m_bits_isValid;

    qint32 m_confirmations;
    bool m_confirmations_isSet;
    bool m_confirmations_isValid;

    QString m_difficulty;
    bool m_difficulty_isSet;
    bool m_difficulty_isValid;

    QString m_hash;
    bool m_hash_isSet;
    bool m_hash_isValid;

    qint32 m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    qint32 m_items_on_page;
    bool m_items_on_page_isSet;
    bool m_items_on_page_isValid;

    QString m_merkle_root;
    bool m_merkle_root_isSet;
    bool m_merkle_root_isValid;

    QString m_next_block_hash;
    bool m_next_block_hash_isSet;
    bool m_next_block_hash_isValid;

    QString m_nonce;
    bool m_nonce_isSet;
    bool m_nonce_isValid;

    qint32 m_page;
    bool m_page_isSet;
    bool m_page_isValid;

    QString m_previous_block_hash;
    bool m_previous_block_hash_isSet;
    bool m_previous_block_hash_isValid;

    qint32 m_size;
    bool m_size_isSet;
    bool m_size_isValid;

    qint32 m_time;
    bool m_time_isSet;
    bool m_time_isValid;

    qint32 m_total_pages;
    bool m_total_pages_isSet;
    bool m_total_pages_isValid;

    qint32 m_tx_count;
    bool m_tx_count_isSet;
    bool m_tx_count_isValid;

    QList<OAIGetBlockV2_200_response_txs_inner> m_txs;
    bool m_txs_isSet;
    bool m_txs_isValid;

    qint32 m_version;
    bool m_version_isSet;
    bool m_version_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetBlockV2_200_response)

#endif // OAIGetBlockV2_200_response_H
