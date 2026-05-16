import { useState } from 'react';
import { Star, Edit2, Trash2, Copy, Check } from 'lucide-react';
import { PromptItem } from '../types';

interface PromptCardProps {
  prompt: PromptItem;
  onToggleFavorite: (id: string) => void;
  onEdit: (prompt: PromptItem) => void;
  onDelete: (id: string) => void;
}

export function PromptCard({ prompt, onToggleFavorite, onEdit, onDelete }: PromptCardProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(prompt.content);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      console.error('Failed to copy');
    }
  };

  // Truncate content for preview
  const truncatedContent = prompt.content.length > 120
    ? prompt.content.substring(0, 120) + '...'
    : prompt.content;

  return (
    <div className="group bg-slate-800 rounded-xl border border-slate-700 overflow-hidden hover:border-violet-500/50 transition-all duration-300 hover:shadow-lg hover:shadow-violet-500/5">
      {/* Card Header */}
      <div className="flex items-start justify-between p-4 border-b border-slate-700">
        <div className="flex-1 min-w-0">
          <h3 className="text-white font-semibold text-lg truncate group-hover:text-violet-300 transition-colors">
            {prompt.title}
          </h3>
          {prompt.description && (
            <p className="text-slate-400 text-sm mt-1 truncate">
              {prompt.description}
            </p>
          )}
        </div>
        <div className="flex items-center gap-1 ml-3">
          {/* Favorite Button */}
          <button
            onClick={() => onToggleFavorite(prompt.id)}
            className={`p-2 rounded-lg transition-all ${
              prompt.isFavorite
                ? 'text-yellow-400 hover:bg-yellow-400/10'
                : 'text-slate-500 hover:text-yellow-400 hover:bg-slate-700'
            }`}
            title={prompt.isFavorite ? '取消收藏' : '收藏'}
          >
            <Star className={`w-5 h-5 ${prompt.isFavorite ? 'fill-current' : ''}`} />
          </button>
          {/* Edit Button */}
          <button
            onClick={() => onEdit(prompt)}
            className="p-2 text-slate-500 hover:text-violet-400 hover:bg-slate-700 rounded-lg transition-all opacity-0 group-hover:opacity-100"
            title="编辑"
          >
            <Edit2 className="w-5 h-5" />
          </button>
          {/* Delete Button */}
          <button
            onClick={() => onDelete(prompt.id)}
            className="p-2 text-slate-500 hover:text-red-400 hover:bg-slate-700 rounded-lg transition-all opacity-0 group-hover:opacity-100"
            title="删除"
          >
            <Trash2 className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Card Body */}
      <div className="p-4">
        {/* Content Preview */}
        <div className="bg-slate-900 rounded-lg p-3 mb-4">
          <p className="text-slate-300 text-sm leading-relaxed whitespace-pre-wrap break-all">
            {truncatedContent}
          </p>
        </div>

        {/* Tags */}
        <div className="flex flex-wrap gap-2 mb-4">
          {prompt.tags.map(tag => (
            <span
              key={tag}
              className="px-2.5 py-1 bg-slate-700 hover:bg-violet-600/30 text-slate-300 hover:text-violet-300 text-xs rounded-full transition-colors cursor-pointer"
            >
              {tag}
            </span>
          ))}
        </div>

        {/* Copy Button */}
        <button
          onClick={handleCopy}
          className={`w-full flex items-center justify-center gap-2 py-3 rounded-lg font-medium transition-all duration-200 ${
            copied
              ? 'bg-green-600 text-white'
              : 'bg-violet-600 hover:bg-violet-700 text-white'
          }`}
        >
          {copied ? (
            <>
              <Check className="w-5 h-5" />
              Copied!
            </>
          ) : (
            <>
              <Copy className="w-5 h-5" />
              复制提示词
            </>
          )}
        </button>
      </div>
    </div>
  );
}

// Empty State Component
interface EmptyStateProps {
  onAddClick: () => void;
  searchTerm?: string;
}

export function EmptyState({ onAddClick, searchTerm }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-20 px-4">
      <div className="w-24 h-24 bg-slate-800 rounded-full flex items-center justify-center mb-6">
        <div className="w-12 h-12 border-2 border-dashed border-slate-600 rounded-full flex items-center justify-center">
          <span className="text-2xl">?</span>
        </div>
      </div>
      <h3 className="text-xl font-semibold text-white mb-2">
        {searchTerm ? '没有找到匹配的提示词' : '还没有任何提示词'}
      </h3>
      <p className="text-slate-400 mb-6 text-center">
        {searchTerm
          ? '试试其他关键词，或者创建一个新的提示词'
          : '开始创建你的第一个 AI 提示词吧'}
      </p>
      <button
        onClick={onAddClick}
        className="flex items-center gap-2 px-6 py-3 bg-violet-600 hover:bg-violet-700 text-white font-medium rounded-xl transition-all"
      >
        <span className="text-lg">+</span>
        创建第一个提示词
      </button>
    </div>
  );
}

// Stats Bar Component
interface StatsBarProps {
  totalCount: number;
  popularTags: string[];
}

export function StatsBar({ totalCount, popularTags }: StatsBarProps) {
  return (
    <div className="flex items-center gap-6 py-4 border-b border-slate-700">
      <div className="flex items-center gap-2">
        <div className="w-2 h-2 bg-violet-500 rounded-full" />
        <span className="text-slate-300">
          <span className="text-white font-semibold">{totalCount}</span> 个提示词
        </span>
      </div>
      {popularTags.length > 0 && (
        <div className="flex items-center gap-2">
          <span className="text-slate-400 text-sm">热门标签:</span>
          <div className="flex flex-wrap gap-2">
            {popularTags.slice(0, 3).map(tag => (
              <span
                key={tag}
                className="px-2 py-1 bg-slate-700 text-slate-300 text-xs rounded-full"
              >
                {tag}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
