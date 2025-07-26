import { useChatContext } from '../context/ChatContext';

const ConversationHistory = () => {
  const { pastConversations, loadConversation } = useChatContext();

  return (
    <div className="w-64 p-4 border-r bg-gray-100 overflow-y-auto">
      <h2 className="text-xl font-semibold mb-4">Past Conversations</h2>

      {pastConversations.length === 0 ? (
        <p className="text-gray-500">No past conversations</p>
      ) : (
        pastConversations.map((conv, i) => (
          <div
            key={conv.id}
            className="cursor-pointer p-2 rounded hover:bg-gray-200 mb-2 bg-white shadow"
            onClick={() => loadConversation(conv.id)}
          >
            Session {conv.id}
          </div>
        ))
      )}
    </div>
  );
};

export default ConversationHistory;
