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

/*
 * OAIGetTransactionInfoResponse.h
 *
 * 
 */

#ifndef OAIGetTransactionInfoResponse_H
#define OAIGetTransactionInfoResponse_H

#include <QJsonObject>

#include "OAIGetTransactionInfoResponse_vin_inner.h"
#include "OAIGetTransactionInfoResponse_vout_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGetTransactionInfoResponse_vin_inner;
class OAIGetTransactionInfoResponse_vout_inner;

class OAIGetTransactionInfoResponse : public OAIObject {
public:
    OAIGetTransactionInfoResponse();
    OAIGetTransactionInfoResponse(QString json);
    ~OAIGetTransactionInfoResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBlockhash() const;
    void setBlockhash(const QString &blockhash);
    bool is_blockhash_Set() const;
    bool is_blockhash_Valid() const;

    double getBlockheight() const;
    void setBlockheight(const double &blockheight);
    bool is_blockheight_Set() const;
    bool is_blockheight_Valid() const;

    double getBlocktime() const;
    void setBlocktime(const double &blocktime);
    bool is_blocktime_Set() const;
    bool is_blocktime_Valid() const;

    double getConfirmations() const;
    void setConfirmations(const double &confirmations);
    bool is_confirmations_Set() const;
    bool is_confirmations_Valid() const;

    double getFee() const;
    void setFee(const double &fee);
    bool is_fee_Set() const;
    bool is_fee_Valid() const;

    QString getHex() const;
    void setHex(const QString &hex);
    bool is_hex_Set() const;
    bool is_hex_Valid() const;

    double getLocktime() const;
    void setLocktime(const double &locktime);
    bool is_locktime_Set() const;
    bool is_locktime_Valid() const;

    double getTime() const;
    void setTime(const double &time);
    bool is_time_Set() const;
    bool is_time_Valid() const;

    double getTotalsent() const;
    void setTotalsent(const double &totalsent);
    bool is_totalsent_Set() const;
    bool is_totalsent_Valid() const;

    QString getTxid() const;
    void setTxid(const QString &txid);
    bool is_txid_Set() const;
    bool is_txid_Valid() const;

    double getVersion() const;
    void setVersion(const double &version);
    bool is_version_Set() const;
    bool is_version_Valid() const;

    QList<OAIGetTransactionInfoResponse_vin_inner> getVin() const;
    void setVin(const QList<OAIGetTransactionInfoResponse_vin_inner> &vin);
    bool is_vin_Set() const;
    bool is_vin_Valid() const;

    QList<OAIGetTransactionInfoResponse_vout_inner> getVout() const;
    void setVout(const QList<OAIGetTransactionInfoResponse_vout_inner> &vout);
    bool is_vout_Set() const;
    bool is_vout_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_blockhash;
    bool m_blockhash_isSet;
    bool m_blockhash_isValid;

    double m_blockheight;
    bool m_blockheight_isSet;
    bool m_blockheight_isValid;

    double m_blocktime;
    bool m_blocktime_isSet;
    bool m_blocktime_isValid;

    double m_confirmations;
    bool m_confirmations_isSet;
    bool m_confirmations_isValid;

    double m_fee;
    bool m_fee_isSet;
    bool m_fee_isValid;

    QString m_hex;
    bool m_hex_isSet;
    bool m_hex_isValid;

    double m_locktime;
    bool m_locktime_isSet;
    bool m_locktime_isValid;

    double m_time;
    bool m_time_isSet;
    bool m_time_isValid;

    double m_totalsent;
    bool m_totalsent_isSet;
    bool m_totalsent_isValid;

    QString m_txid;
    bool m_txid_isSet;
    bool m_txid_isValid;

    double m_version;
    bool m_version_isSet;
    bool m_version_isValid;

    QList<OAIGetTransactionInfoResponse_vin_inner> m_vin;
    bool m_vin_isSet;
    bool m_vin_isValid;

    QList<OAIGetTransactionInfoResponse_vout_inner> m_vout;
    bool m_vout_isSet;
    bool m_vout_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetTransactionInfoResponse)

#endif // OAIGetTransactionInfoResponse_H
