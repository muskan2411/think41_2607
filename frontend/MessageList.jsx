import { useChatContext } from '../context/ChatContext';
import Message from './Message';

const MessageList = () => {
  const { messages } = useChatContext();
  return (
    <div className="flex-1 p-4 overflow-y-auto">
      {messages.map((msg, i) => (
        <Message key={i} message={msg} />
      ))}
    </div>
  );
};

export default MessageList;
